import json


def create_technologies_file():
    file = open('./preprocessed_sharepoint_data.json', 'r')
    technologies_file = open('../stackexchange/op.tags.csv', 'w')
    technologies_file.write(",tagname,tagcount\n")
    content = file.read()
    onepagers = json.loads(content)
    for onepager in onepagers:
        tech_array_arry = onepager.get('technologien')
        if tech_array_arry is not None:
            for tech_array in tech_array_arry:
                for technology in tech_array:
                    for tech_term in technology.split(" "):
                        technologies_file.write(f"\"\",\"{tech_term}\",\"1\"\n")
    technologies_file.close()


if __name__ == "__main__":
    create_technologies_file()
