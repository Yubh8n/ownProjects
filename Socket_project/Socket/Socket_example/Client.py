#!/usr/bin/env python3

import socket
from time import sleep

i = 0
HOST = '192.168.8.108'  # The server's hostname or IP address
PORT = 65433        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"test")
        sleep(0.1)
        i+= 1
        data = s.recv(1024)

        print('Received', repr(data))