#!/usr/bin/python3

import socket
from math import sqrt

class pr5 ():
    def __init__(self):
        self = self

    def soma (self,a,b):
        x = float(a)+float(b)
        return str(x)

    def raiz_quadrada (self, a):
        x = sqrt(float(a))
        return str(x)

HOST = socket.gethostbyname('localhost')
PORT = 3001

tcp_ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_ss.bind((HOST,PORT))
tcp_ss.listen(1)

func = pr5()

client, addr = tcp_ss.accept()

def send_msg(msg):
    message = msg
    message = msg.encode('utf-8')
    client.send(message)

while True:
    message = client.recv(1024)
    message = message.decode('utf-8')

    wtodo = message.split(' ')
    if wtodo[0] == 'soma':
        send_msg(func.soma(wtodo[1],wtodo[2]))
    elif wtodo[0] == 'raiz_quadrada':
        send_msg(func.raiz_quadrada(wtodo[1]))
    else:
        send_msg('Mensagem invalida')
tcp_ss.close()