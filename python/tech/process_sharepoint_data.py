import json
import os


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


def create_files():
    file = open("./preprocessed_sharepoint_data.json", "r")
    content = file.read()
    onepagers = json.loads(content)
    for onepager in onepagers:
        name = onepager.get("name")
        onepager_file = open(os.path.join("out", f"{name}.txt"), "w")
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
