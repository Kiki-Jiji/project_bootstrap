from .file_classes import Folder, File

def create_file_list(struct):

    files_list = []
    for file_struct in struct["files"]:
        file_info = struct["files"][file_struct]
        file_to_create = convert_to_file(file_info)
        files_list.append(file_to_create)

    return files_list

def convert_to_folder(struct: dict, files_in_folder):
     return Folder(name = struct["name"], files= files_in_folder)

def is_template(string: str):
    return "_template" in string

def strip_all_puncation(string: str):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join([i for i in string if i not in punctuation])
