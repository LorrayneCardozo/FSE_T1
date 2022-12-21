from central.server import socketCentral
from log.log import escreverLog

def menu(ip:str, porta:int):
    while True:
        print('\n------------ MENU ------------')
        print('Qual sala deseja acessar?')
        print('1 - Sala 01')
        print('2 - Sala 02')
        
        sala = input()

        opcoes = ['0 - Visualizar estados', '1 - Ligar/desligar lâmpada 1', '2 - Ligar/desligar lâmpada 2', '3 - Ligar/desligar projetor', '4 - Ligar/desligar ar-condicionado', '5 - Ligar/desligar alarme', '6 - Ligar/desligar sensor de presença', '7 - Ligar/desligar sensor de fumaça', '8 - Ligar/desligar sensor de janela', '9 - Ligar/desligar sensor de porta', '10 - Ligar/desligar sensor de contagem de entradas', '11 - Ligar/desligar sensor de contagem de saídas', '12 - Visualizar temperatura e umidade']
        print(f'\n------------ SALA {sala} ------------')
        print("Escolha uma opção:")
        print('\n'.join(opcoes))
        escolha = int(input())
        msg = sala + ' ' + opcoes[escolha]
        escreverLog(opcoes[escolha][4:] + ' da sala ' + sala)
        socketCentral(ip, porta, msg)