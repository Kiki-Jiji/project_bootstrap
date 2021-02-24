import argparse
import project_bootstrap as pb
import os
import yaml
import shutil
import subprocess
from project_bootstrap import Folder, File



parser = argparse.ArgumentParser()

parser.add_argument("project_name", 
                    help="The name of the project. The name the folder created is given.",
                    type=str)

parser.add_argument("author", 
                    help="The author('s) or creator of the project. ",
                    type=str)

parser.add_argument("author_email", 
                    help="The author('s) or creator of the project email address. ",
                    type=str)

parser.add_argument("description", 
                    help="Descrption of the project ",
                    type=str)

parser.add_argument("--git", 
                    help="Initalises git",
                    action="store_true")

args = parser.parse_args()

project_name = args.project_name
author = args.author
author_email = args.author_email
description = args.description
git = args.git



ignore = {
    "type": "file",
    "name": "ignore.txt",
    "contents": "ignore this file",
}

project_config = {
    "gitignore": {
        "type": "file",
        "name": ".gitignore",
        "contents": "gitignore"
    },
    "readme": {
        "type": "file",
        "name": "README.md",
        "contents": "# README",
    },
    "requirements": {
        "type": "file",
        "name": "requirements.txt",
        "contents": "# add packages in here",
    },
    "data": {
        "type": "folder",
        "name": "data",
        "files": {
            "ignore": ignore
        }
    },
    "docs": {
        "type": "folder",
        "name": "docs",
        "files": {
            "ignore": ignore
        }
    },
    "analysis": {
        "type": "folder",
        "name": "analysis",
        "files": {
            "ignore": ignore
        }
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
    },
    "setup": {
        "type": "file",
        "name": "setup.py",
        "contents": "setup",
        "args": {
            "package_name": project_name,
            "author": author,
            "author_email": author_email,
            "description": description
        }     
    }
}


def main(project_name, project_config, git):


    os.mkdir(project_name)

    if git is True:
        subprocess.run("git init", shell="True", capture_output=True, cwd=project_name)

    project = pb.ProjectBootstrap(project_name, config=project_config)

    project.parse_project_structure()

    project.create_project()


if __name__ == '__main__':
    main(project_name, project_config, git)

