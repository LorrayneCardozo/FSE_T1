import json

def json_to_object(dir):
    file = open(dir, encoding='utf-8')
    data = json.load(file)
    file.close()
    
    return data

def gravar(data):
    dir = './json_files/estados.json'
    file = open(dir, 'w')
    json.dump(data, file)
    file.close()