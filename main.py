##### This creates and deletes a project
# an hacky intergration test if you will :P


import project_bootstrap as pb
import os
import yaml
import shutil

from project_bootstrap import Folder, File


# # temp store- remember to create/delete
temp = "temp"
os.mkdir(temp)

project = pb.ProjectBootstrap(temp, config= "test_config.yaml")

project.parse_project_structure()
project.create_project()

shutil.rmtree(temp)

print("finished")