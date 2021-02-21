import os
from .file_classes import File, Folder

class ProjectBootstrap:

    project_root = None

    def __init__(self, project_root: str = None):
        self.set_project_root(project_root)

    def create_setup(self, file_name: str, package_name: str, author_email: str, description: str):
        file_name = "setup.py"
        template = pb.templates["setup.py"](package_name, author, author_email, description)

        with open(file_name, "w") as open_file:
            open_file.write(template)

    def make_file(self, file_info, folder = None):
        assert isinstance(file_info, File)

        if folder is None:
            file_path = self.project_root + "/" + file_info.name 
        else:
            file_path = self.project_root + "/" + folder.name + "/" + file_info.name

        contents = file_info.contents 
        if contents is None: contents = ""

        with open(file_path, "w") as open_file:
            open_file.write(contents)

    def make_folder(self, folder_info):
        assert isinstance(folder_info, Folder)

        # TODO strip / folder_info.path maybe also name?

        if folder_info.root is True:
            folder_path = self.project_root + "/" + folder_info.name
        elif folder_info.root is False:
            folder_path = self.project_root + "/" + folder_info.path + "/" + folder_info.name
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
                self.make_file(file, folder_info)
        except TypeError:
            self.make_file(folder_info.files, folder_info)




    def create_directory(self, directory_name: str):
        os.mkdir(self.project_root + "/" + directory_name)

    def create_file(self, file_name: str, contents: dict):
        file_path = self.project_root + "/" + file_name

        with open(file_path, "w") as open_file:
            open_file.write(contents)

    def create_init(self, path: str, empty: bool = True):
        file_name = self.project_root + "/" + path + "/__init__.py"
        open(file_name, "x") 

    def set_project_root(self, project_root: str = None):

        if project_root is None:
            project_root = "./"
            print(f"Non project root supplied, setting to current working directory: \n {os.getcwd()}")

        self.project_root = project_root

    
