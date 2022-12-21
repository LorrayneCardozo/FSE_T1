import json
import socket
from json_files.parse_json.json_to_object import gravar

def socketCentral(ip: str, porta:int, msg:str):
    
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, porta)
    tcp.connect(address)
    tcp.send (msg.encode())
    received = json.loads(tcp.recv(8192).decode("utf-8"))
    tcp.close()
    gravar(received)