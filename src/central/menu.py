from central.server import socketCentral
from log.log import escreverLog

def menu():
    while True:
        print('\n------------ MENU ------------')
        print('Qual sala deseja acessar?')
        print('1 - Sala 01')
        print('2 - Sala 02')
        
        sala = input()

        opcoes = ['0 - Visualizar estados', '1 - Ligar/desligar lâmpada 1', '2 - Ligar/desligar lâmpada 2', '3 - Ligar/desligar projetor', '4 - Ligar/desligar ar-condicionado', '5 - Ligar/desligar alarme', '6 - Visualizar temperatura e umidade']
        print(f'\n------------ SALA {sala} ------------')
        print("Escolha uma opção:")
        print('\n'.join(opcoes))
        escolha = int(input())
        msg = sala + ' ' + opcoes[escolha]
        escreverLog(opcoes[escolha][4:] + ' da sala ' + sala)
        socketCentral('164.41.98.26', 10772, msg)