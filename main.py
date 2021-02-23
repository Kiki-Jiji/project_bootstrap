import project_bootstrap as pb
import os
import yaml
import shutil

from project_bootstrap import Folder, File


from dynamic import dynamic_templates


# # temp store- remember to create/delete
temp = "temp"
os.mkdir(temp)

project = pb.ProjectBootstrap(temp)

project.parse_project_structure()
project.create_project()

shutil.rmtree(temp)
