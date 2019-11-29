import json
import os
import re


from util.util import open_file_for_writing_with_path_creation


def write_string(property_name: str, onepager, onepager_file):
    string = onepager.get(property_name)
    if string is not None and len(string) > 0:
        onepager_file.write(string)
        onepager_file.write("\n")


def write_array(property_name: str, onepager, onepager_file):
    array = onepager.get(property_name)
    if array is not None:
        onepager_file.write(" ".join(list(array)))
        onepager_file.write("\n")


def write_double_array(property_name: str, onepager, onepager_file):
    double_array = onepager.get(property_name)
    if double_array is not None:
        for array in double_array:
            onepager_file.write(" ".join(list(array)))
            onepager_file.write("\n")


def custom_key(string: str):
    return -len(string), string.lower()


def normalize(string: str):
    return re.sub('[^A-Za-z0-9]+', '', string).lower()


def folder_name(name: str) -> str:
    folder_names = [line.rstrip('\n') for line in open('./foldernames.txt')]
    sorted_folder_names = sorted(folder_names, key=custom_key)
    for folder_name in sorted_folder_names:
        if normalize(name).startswith(normalize(folder_name)):
            return folder_name
    return '_DEFAULT'


def create_files():
    file = open("./preprocessed_sharepoint_data.json", "r")
    content = file.read()
    onepagers = json.loads(content)
    for onepager in onepagers:
        name = onepager.get("name")
        onepager_filename = os.path.join("out", folder_name(name), f"{name}.txt")
        onepager_file = open_file_for_writing_with_path_creation(onepager_filename)
        write_array('projekt', onepager, onepager_file)
        write_array('PRkunde', onepager, onepager_file)
        write_double_array('technologien', onepager, onepager_file)
        write_array('herausforderung', onepager, onepager_file)
        write_array('lösung', onepager, onepager_file)
        write_array('mehrwert', onepager, onepager_file)
        write_array('schlagworte', onepager, onepager_file)
        write_string('beschreibung', onepager, onepager_file)
        write_array('kompetenzbereich', onepager, onepager_file)
        onepager_file.close()


if __name__ == "__main__":
    create_files()
