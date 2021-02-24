import argparse
import project_bootstrap as pb
import os
import yaml
import shutil

from project_bootstrap import Folder, File



parser = argparse.ArgumentParser()

parser.add_argument("project_name", 
                    help="The name of the project. The name the folder created is given.",
                    type=str)

args = parser.parse_args()

print(args.project_name)

project_name = args.project_name


project_config = {
    "gitignore": {
        "type": "file",
        "name": ".gitignore",
        "contents": "gitignore"
    },
    "test_file": {
        "type": "file",
        "name": "test.txt",
        "contents": "hi there!"
    },
    project_name: {
        "type": "folder",
        "name": project_name,
        "files": {
            "init": {
                "type": "file",
                "name": "__init__.py",
                "contents": "# init"
            }
        }
    }

}



def main(project_name, project_config):

    os.mkdir(project_name)

    project = pb.ProjectBootstrap(project_name, config=project_config)

    project.parse_project_structure()

    project.create_project()


if __name__ == '__main__':
    main(project_name, project_config)