from distribuido.estados import *
from distribuido.sensores.dht22 import temperatura_umidade
from json_files.parse_json.json_to_object import json_to_object


def comando(sala, opcao):

    if(opcao=='0'):
        visualizarEstados(sala)
    elif(opcao=='6'):
        temperatura_umidade(sala)
    else:
        dir = f'./json_files/sala_0{sala}.json'
        data = json_to_object(dir)
        pino = data['outputs'][int(opcao)-1]['gpio']
        alterarEstadoOutputs(sala, pino, int(opcao)-1)