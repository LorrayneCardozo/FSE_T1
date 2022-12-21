import json
from central.menu import menu
import signal
from threading import Thread
import sys
from signal import signal, SIGPIPE, SIG_DFL


def main():
    signal(SIGPIPE,SIG_DFL)
    ip = sys.argv[1]
    porta = sys.argv[2]
    sock = Thread(target=menu, args=(ip, int(porta)))
    sock.start()
    sock.join()

if __name__ == '__main__':
    main()
    