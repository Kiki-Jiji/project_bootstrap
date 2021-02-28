import pytest
from project_bootstrap import ProjectBootstrap
from testing_functions import Test
import os

test = Test(interactive = False)

def test_project_folder_created():
    pb = ProjectBootstrap(**test.config())
    assert not os.path.exists(test.test_folder), "folder not created when class initalised"

    pb.parse_project_structure()
    assert not os.path.exists(test.test_folder), "folder not created when project parsed"

    pb.create_project()
    assert os.path.exists(test.test_folder), "folder created when project created"
