import pytest
import os
from testing_functions import Test

from project_bootstrap import ProjectBootstrap
from project_bootstrap import File, Folder

test = Test(interactive = False)

def test_parse_project():

    pb = ProjectBootstrap(**test.config())

    pb.parse_project_structure()

    pff = pb.project_files_folder

    assert isinstance(pb.project_structure, dict), "project_structure stored as a dict"

    assert isinstance(pff, list), "project_files_folder stored as a list"

    first_item = pff[0]
    assert isinstance(first_item, File), "project_files_folder stored as a list"

    assert first_item.name == '.gitignore'
    assert first_item.contents[0:10] == '# Byte-com', "contenets loaded from template"

    test.cleanup()