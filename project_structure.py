import project_bootstrap as pb
import os

# package_name needs to be the same as directory_name

def create_setup():
    file_name = "setup.py"

    package_name = "python_exampple"
    author = "Joshua"
    author_email = "blank"
    description = "blank_des"

    template = pb.templates["setup.py"](package_name, author, author_email, description)

    with open(file_name, "w") as open_file:
        open_file.write(template)

def create_directory(directory_name):
    os.mkdir(directory_name)

def create_init(path, empty = True):
    file_name = path + "/__init__.py"
    open(file_name, "x") 

