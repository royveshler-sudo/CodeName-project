__author__ = "ROY"


import socket
import threading


clt_sock = socket.socket()
clt_sock.connect(('127.0.0.1', 2174))
print('Connected to server')

