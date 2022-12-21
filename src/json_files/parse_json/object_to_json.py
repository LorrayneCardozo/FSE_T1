import json

def object_to_json(data):
    dir = './json_files/estados.json'
    json_object = json.dumps(data, indent=4)
    with open(dir, "w") as outfile:
        outfile.write(json_object)