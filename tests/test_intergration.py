import pytest
import project_bootstrap as pb
import os
from testing_functions import Test

test = Test()

def main(config):
    project = pb.ProjectBootstrap(test.test_folder, config, template_location="templates")
    project.parse_project_structure()
    project.create_project()

def test_intergration_with_yaml():

    main("tests/test_config.yaml")
    test_folder = test.test_folder

    assert os.path.exists(test_folder) is True, f"project folder should be created, called {test_folder}"

    ff = ['setup.py', '.gitignore', 'special.txt', 'data']
    assert os.path.exists(test_folder + "/" + ff[0]) is True, f"file/folder should be created, called {ff[0]}"
    assert os.path.exists(test_folder + "/" + ff[1]) is True, f"file/folder should be created, called {ff[1]}"
    assert os.path.exists(test_folder + "/" + ff[2]) is True, f"file/folder should be created, called {ff[2]}"
    assert os.path.exists(test_folder + "/" + ff[3]) is True, f"file/folder should be created, called {ff[3]}"

    test.cleanup()

def test_intergration_dict_config():

    project_name = "project_test"
    author = "tester"
    author_email = "tester@gmail.com"
    description = "A project for testing"

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
        "docs": {
        "type": "folder",
        "name": "docs",
        "files": {
            "ignore": {
                "type": "file",
                "name": "ignore.txt",
                "contents": "ignore this file",
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

    main(project_config)

    top_level = [file for file in project_config.keys()]

    for file in top_level:
        file_name = project_config[file]["name"]
        assert os.path.exists(test.test_folder + "/" + file_name) is True, f"file/folder should be created, called {file_name}" 

    assert os.path.exists(test.test_folder + "/docs/ignore.txt"), "ignore.txt should be created inside docs"

    test.cleanup()