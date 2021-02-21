import project_bootstrap as pb
import os
import yaml

from project_bootstrap import Folder, File

# exmaple files/folders
init = File("__init__.py")
python_package = Folder("example_package", [init])

placeholder = File("ignore.txt", "ignore this file")
data_folder = Folder("data", files = placeholder)


project = [python_package, data_folder]

# temp store- remember to create
os.mkdir("temp")
temp = "temp"

# Try with data_folder
project = pb.ProjectBootstrap(temp)
project.make_folder(data_folder)

# read yaml
