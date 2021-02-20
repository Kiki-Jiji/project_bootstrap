
def create_setup(file_name: str, package_name: str, author_email: str, description: str):
    file_name = "setup.py"

    package_name = "python_exampple"
    author = "Joshua"
    author_email = "blank"
    description = "blank_des"

    template = pb.templates["setup.py"](package_name, author, author_email, description)

    with open(file_name, "w") as open_file:
        open_file.write(template)

def create_directory(directory_name: str):
    os.mkdir(directory_name)

def create_init(path str, empty = True: bool):
    file_name = path + "/__init__.py"
    open(file_name, "x") 
