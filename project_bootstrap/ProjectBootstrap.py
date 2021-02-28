import os
import yaml
import subprocess

from .file_classes import File, Folder
from.ProjectBootstrap_functions_generics import *
from typing import Union

from dynamic import dynamic_templates

class ProjectBootstrap:

    project_name = None

    project_root = None

    project_structure = None

    project_files_folder = None

    template_location = None

    def __init__(self, project_root: str = None, project_name: str = None, config: str = None, template_location: str = None):

        self.set_project_name(project_name)
        self.set_template_location(template_location)
        self.set_project_root(project_root)
        self.set_project_config(config)

    def create_file(self, file_info, folder = None):
        assert isinstance(file_info, File)

        project_location = self.project_root + "/" + self.project_name + "/"

        if folder is None:
            file_path = project_location+ file_info.name 
        else:
            file_path = project_location + folder.name + "/" + file_info.name

        contents = file_info.contents 
        if contents is None: contents = ""

        with open(file_path, "w") as open_file:
            open_file.write(contents)

    def create_folder(self, folder_info):
        assert isinstance(folder_info, Folder)

        # TODO strip / folder_info.path maybe also name?

        project_location = self.project_root + "/" + self.project_name + "/"

        if folder_info.root is True:
            folder_path = project_location + folder_info.name
        elif folder_info.root is False:
            folder_path = project_location + folder_info.path + "/" + folder_info.name
        else:
            raise ValueError(f"Folder.root needs to be a boolean, so only True or False are allowed. The actual value was {folder_info.root}")

        # make the folder
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            print("Folder already exists")

        # make any files
        try:
            for file in folder_info.files:
                self.create_file(file, folder_info)
        except TypeError:
            self.create_file(folder_info.files, folder_info)

    def create_project(self, git: bool=False):

        if self.project_files_folder is None:
            self.parse_project_structure()

        self.create_project_folder()

        if git is True:
            self.init_git()

        for struct in self.project_files_folder:

            if isinstance(struct, File):
                self.create_file(struct)

            elif isinstance(struct, Folder):
                self.create_folder(struct)
            else:
                raise ValueError("project_files_folder contains an element which is not of class File or Folder. This isn't supported")

    def set_project_config(self, config: Union[str, dict] = None):

        if config is None:
            config = "project_config.yaml"

        elif isinstance(config, str):
            config = config

        elif isinstance(config, dict):
            self.project_structure = config

        else:
            raise ValueError("Please provide either a str with the path to a valid config or provide a config in the form of a dict")

        if isinstance(config, str):
            with open(config) as conf:
                self.project_structure = yaml.load(conf)

    def parse_project_structure(self):

        if self.project_structure is None:
            return("project_structure is not set. Use ProjectBootstrap.set_project_config")

        project_files_folders = []

        for file in self.project_structure:

            struct = self.project_structure[file]

            if struct["type"] == "file":
                file_to_create = self.convert_to_file(struct)
                project_files_folders.append(file_to_create)
            elif struct["type"] == 'folder':
                files_in_folder =  self.create_file_list(struct)
                folder_to_create = convert_to_folder(struct, files_in_folder)
                project_files_folders.append(folder_to_create)
            else:
                print("incorrect type")

        self.project_files_folder = project_files_folders
        
    def set_project_root(self, project_root: str = None):
        """
        Project Root, the location where the project is to be created, as in a folder with the project name gets created in this location
        """
        if project_root is None:
            project_root = "./"
            print(f"No project root supplied, setting to current working directory: \n {os.getcwd()}")

        self.project_root = project_root


    def set_project_name(self, project_name: str):
        if project_name is None:
            raise ValueError("No project name supplied")

        self.project_name = project_name


    def set_template_location(self, template_location: str = None):

        if template_location is None:
            template_location = "templates"

        self.template_location = template_location

    def load_template(self, struct):

        seperator = "_"

        file_name_stripped = struct["contents"].replace(".py", "")

        template_stripped = file_name_stripped.split(seperator)[0]

        available_templates = os.listdir(self.template_location)

        available_templates_stripped = [temp.split(seperator)[0] for temp in available_templates]

        # read dynamic
        if 'args' in struct.keys():
            if template_stripped in dynamic_templates:
                dynamic_template_func = dynamic_templates[template_stripped]
                template_string = dynamic_template_func(**struct["args"])
                return template_string
            else:
                print("file config indicates it is dynmaic by containing args but no dynamic template is available")

        # if dynamic (contains args) but no dynamic template is found give it another go looking for static
        if template_stripped in available_templates_stripped:
            template_string = self.read_template(available_templates[available_templates_stripped.index(template_stripped)])
        else:
            print(f"No template found matching {struct['name']}")
            template_string = None

        return template_string

    def read_template(self, template_name: str):

        path = self.template_location + "/" + template_name

        with open(path, "r") as file:
            template_text = file.read()

        return template_text

    def convert_to_file(self, struct: dict):

        file_name = struct["name"].replace(".py", "")
        file_name = strip_all_puncation(file_name)

        if struct["contents"] == file_name or is_template(struct["contents"]):
            contents = self.load_template(struct)
        else:
            contents = struct["contents"]

        file_struct = File(struct["name"], contents)
        return file_struct

    def create_file_list(self, struct):

        files_list = []
        for file_struct in struct["files"]:
            file_info = struct["files"][file_struct]
            file_to_create = self.convert_to_file(file_info)
            files_list.append(file_to_create)

        return files_list

    def create_project_folder(self):
        try:
            os.mkdir(self.project_root + "/" + self.project_name)
        except:
            print("folder already exists, using existing folder")

    def init_git(self):
        subprocess.run("git init", shell="True", capture_output=True, cwd=self.project_root + "/" + self.project_name)




        
