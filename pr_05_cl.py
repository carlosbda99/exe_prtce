#!/usr/bin/python3

import socket

HOST = socket.gethostbyname('localhost')
PORT = 3001

tcp_sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_sc.connect((HOST,PORT))

while True:
    message = input()
    message = message.encode('utf-8')
    tcp_sc.send(message)
    
    message = tcp_sc.recv(1024)
    message = message.decode('utf-8')
    print ('Resultado: ', message)

tcp_sc.close()