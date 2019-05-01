#!/usr/bin/env python3

import socket
import _thread
import sys


def on_new_client(clientsocket, addr):
    while True:
        try:
            msg = clientsocket.recv(1024)
            if len(msg) > 0:
                string = ord(msg)
                print(string)
            else:
                break
        except socket.error:
            print("you had one job!")
            clientsocket.close()


try:
    PORT = 65433
    s = socket.socket()
    HOST = "192.168.8.109"
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        c, addr = s.accept()
        _thread.start_new_thread(on_new_client, (c, addr))
except KeyboardInterrupt as msg:
    sys.exit(0)
s.close()




'''#!/usr/bin/env python3

import socket
import codecs
from time import sleep
import thread

HOST = '192.168.8.109'
PORT = 65433
prev_data = 0


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                #stri =data.decode('unicode_escape')
                if not data:
                    break
                string = ord(data)
                print(string)'''