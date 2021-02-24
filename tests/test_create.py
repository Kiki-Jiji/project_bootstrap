import pytest
import project_bootstrap as pb
import os
import shutil

test_folder = "temporary_test_folder"

# def setup():
#     try:
#         os.mkdir(test_folder)
#     except FileExistsError:
#         shutil.rmtree(test_folder)
#         os.mkdir(test_folder)

#     test_project = pb.ProjectBootstrap(test_folder)
#     return test_project
    
def cleanup():
    shutil.rmtree(test_folder)

def main(config):
    project = pb.ProjectBootstrap(test_folder, config, template_location="templates")
    project.parse_project_structure()
    project.create_project()

def test_intergration_with_yaml():

    main("tests/test_config.yaml")

    assert os.path.exists(test_folder) is True, f"project folder should be created, called {test_folder}"

    ff = ['setup.py', '.gitignore', 'special.txt', 'data']
    assert os.path.exists(test_folder + "/" + ff[0]) is True, f"file/folder should be created, called {ff[0]}"
    assert os.path.exists(test_folder + "/" + ff[1]) is True, f"file/folder should be created, called {ff[1]}"
    assert os.path.exists(test_folder + "/" + ff[2]) is True, f"file/folder should be created, called {ff[2]}"
    assert os.path.exists(test_folder + "/" + ff[3]) is True, f"file/folder should be created, called {ff[3]}"

    cleanup()

# def test_create_init():
    
#     test_config = {
#         pass
#     }

#     main()
    
#     cleanup()