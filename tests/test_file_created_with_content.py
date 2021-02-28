import pytest
from project_bootstrap import ProjectBootstrap
from testing_functions import Test
import os

test = Test(interactive = True)

def test_file_created_text():

    conf = test.config()

    files = {
        "test_file": {
            "type": "file",
            "name": "file_with_text.txt",
            "contents": "This is some text"
        }
    }

    conf["config"] = files

    pb = ProjectBootstrap(**conf)
    pb.parse_project_structure()
    pb.create_project()

    file_name = conf["project_root"] + "/" + conf["config"]["test_file"]["name"]

    assert os.path.exists(file_name)

    with open(file_name, "r") as f:
        file = f.read()

    assert file == conf["config"]["test_file"]["contents"], "contents of file is correct" 
    
def test_file_created_static_template():
    pass


def test_file_created_dynamic_template():
    pass
