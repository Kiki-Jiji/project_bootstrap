'''
A simple Gooey example. One required field, one optional.

Run with pythonw gui.py
'''

from gooey import Gooey, GooeyParser
import argparse
import project_bootstrap as pb
import os
import yaml
import shutil
import subprocess
from project_bootstrap import Folder, File

@Gooey()
def main():
    parser = GooeyParser(description='Process some integers.')

    parser.add_argument(
        'required_field',
        metavar='Some Field',
        help='Enter some text!')

    parser.add_argument(
        '-f', '--foo',
        metavar='Some Flag',
        action='store_true',
        help='I turn things on and off')

    parser.parse_args()
    print('Hooray!')

    project = pb.ProjectBootstrap()

    project.parse_project_structure()

    project.create_project()

if __name__ == '__main__':
    main()