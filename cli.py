import argparse
import project_bootstrap as pb
import os
import yaml
import shutil
import subprocess
from project_bootstrap import Folder, File, project_structure


def main(project_name, project_config, git):


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


    project_config = project_structure(project_name, author, author_email, description)

    if git is True:
        subprocess.run("git init", shell="True", capture_output=True, cwd=project_name)

    project = pb.ProjectBootstrap(project_name, config=project_config)

    project.parse_project_structure()

    project.create_project()


if __name__ == '__main__':
    main(project_name, project_config, git)

