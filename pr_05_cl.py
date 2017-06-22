#!/usr/bin/python3

import socket

HOST = socket.gethostbyname('localhost')
PORT = 3000

tcp_sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_sc.connect((HOST,PORT))

message = input()
message = message.encode('utf-8')
tcp_sc.send(message)

message = tcp_sc.recv(2048)
message = message.decode('utf-8')
print (message)

tcp_sc.close()
