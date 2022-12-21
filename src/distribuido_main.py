from distribuido.server import socketDistribuido
import json
from threading import Thread
import sys
from signal import signal, SIGPIPE, SIG_DFL
from json_files.parse_json.json_to_object import json_to_object

def main():
    print("---------- INICIANDO SERVIDOR DISTRIBUIDO ------------")
    sala1 = json_to_object(f'json_files/sala_01.json')
    ip= str(sala1["ip_servidor_distribuido"])
    porta= int(sala1["porta_servidor_distribuido"])
    
    sock = Thread(target=socketDistribuido, args=(ip, int(porta)))
    
    sock.start()
    

if __name__ == '__main__':
    main()
   