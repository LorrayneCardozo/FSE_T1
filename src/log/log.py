from datetime import datetime

def escreverLog(mensagem):
    log = open("log/log.csv", "a")
    log.write(f"{datetime.now()} - {mensagem}\n")
    log.close()
