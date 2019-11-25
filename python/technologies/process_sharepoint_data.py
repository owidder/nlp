import json
import os

file = open("./preprocessed_sharepoint_data.json", "r")
content = file.read()

onepagers = json.loads(content)

for onepager in onepagers:
    name = onepager.get("name")
    onepager_file = open(os.path.join("out", f"{name}.txt"), "w")
    projekt = onepager.get("projekt")
    if projekt is not None:
        onepager_file.write(" ".join(list(onepager.get("projekt"))))
    onepager_file.close()
