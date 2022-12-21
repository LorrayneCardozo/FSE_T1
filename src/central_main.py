import json
from central.menu import menu
import signal
from threading import Thread
import sys
from signal import signal, SIGPIPE, SIG_DFL


def main():
    signal(SIGPIPE,SIG_DFL)
    sock = Thread(target=menu)
    sock.start()
    sock.join()

if __name__ == '__main__':
    main()
    