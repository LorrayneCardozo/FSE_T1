import json
from distribuido.sensores.outputs import outputs
from json_files.parse_json.json_to_object import json_to_object
from json_files.parse_json.object_to_json import object_to_json

def visualizarEstados(sala):
    dir = './json_files/estados.json'
    data = json_to_object(dir)
    print('\n')
    print(f'\n------------ ESTADOS - SALA {sala} ------------')
    for i in range(5):
        print(f"{data['sala_0'+sala][0]['outputs'][i]['name'].capitalize()}: {data['sala_0'+sala][0]['outputs'][i]['status']}")

def alterarEstadoOutputs(sala, pino, indice):
    dir = './json_files/estados.json'
    data = json_to_object(dir)
    data['sala_0'+sala][0]['outputs'][indice]['status'] = outputs(pino)
    object_to_json(data)