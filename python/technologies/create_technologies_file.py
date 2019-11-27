import json


def create_technologies_file():
    file = open('./preprocessed_sharepoint_data.json', 'r')
    technologies_file = open('./technologies.txt', 'w')
    content = file.read()
    onepagers = json.loads(content)
    for onepager in onepagers:
        tech_array_arry = onepager.get('technologien')
        if tech_array_arry is not None:
            for tech_array in tech_array_arry:
                technologies_file.write("\n".join(list(tech_array)))
                technologies_file.write("\n")
    technologies_file.close()


if __name__ == "__main__":
    create_technologies_file()
