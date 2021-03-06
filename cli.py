import argparse
from gooey import Gooey, GooeyParser

from project_bootstrap import project_structure, ProjectBootstrap


@Gooey(program_name="EMR Project Quickstart", advanced=True)
def main():

    parser = GooeyParser(description ="Jumpstart a python project")

    parser.add_argument("project_location",
                        help="Where you want the project to be created",
                        widget="DirChooser")

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
    project_location = args.project_location

    project_config = project_structure(project_name, author, author_email, description)

    project = ProjectBootstrap(project_root = project_location,
                                project_name= project_name,
                                config=project_config).create_project(git)

if __name__ == '__main__':
    main()

