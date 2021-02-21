import pytest
import project_bootstrap as pb
import os
import shutil

test_folder = "temporary_test_folder"

def setup():
    try:
        os.mkdir(test_folder)
    except FileExistsError:
        shutil.rmtree(test_folder)
        os.mkdir(test_folder)

    test_project = pb.ProjectBootstrap(test_folder)
    return test_project
    
def cleanup():
    shutil.rmtree(test_folder)

def test_create_directory():
    test_project = setup()
    folder = "test1"
    test_project.create_directory(folder)

    assert os.path.exists(test_folder + "/" + folder)
    cleanup()

def test_create_init():
    test_project = setup()
    test_project.create_init("./")
    assert os.path.exists(test_folder + "/__init__.py")
    cleanup()