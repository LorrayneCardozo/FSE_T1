import sys,os,signal
import json
import pprint
import socket
import socketserver
from distribuido.comandos import comando

def socketDistribuido(ip: str, porta:int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, porta))
    sock.listen(1)
    while True:
        con, cliente = sock.accept()
        print ('Conectado por', cliente)
        while True:
            msg = con.recv(8192)
            if not msg: break
            temp = msg.decode()
            print(temp)
            sala = temp[0]
            opcao = temp[2]
            estados = comando(sala, opcao)
            con.sendall(bytes(json.dumps(estados), encoding="UTF-8"))
        print ('Finalizando conexao do cliente', cliente)