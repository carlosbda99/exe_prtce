#!/usr/bin/python3
'''Faça o teste com
soma 3 bola\nsoma 2 3\nraiz_quadrada 9
Assim foi pedido, comando + arg +\n = varias solicitacoes
'''


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
PORT = 3000

tcp_ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_ss.bind((HOST,PORT))
tcp_ss.listen(1)

func = pr5()

client, addr = tcp_ss.accept()

def send_msg(msg):
	message = msg
	message = msg.encode('utf-8')
	client.send(message)

message = client.recv(1024)
message = message.decode('utf-8')

inst = message.split('\\n')
resp = ''
print (message)

for x in inst:
	wtodo = x.split(' ')
	if wtodo[0] == 'soma' and wtodo[1].isnumeric() and wtodo[2].isnumeric():
		resp += ('Resultado de %s + %s: '%(wtodo[1],wtodo[2])) + (func.soma(wtodo[1],wtodo[2])) + '\n'
	elif wtodo[0] == 'raiz_quadrada' and wtodo[1].isnumeric():
		resp += ('Resultado da raiz de %s: '%wtodo[1]) + (func.raiz_quadrada(wtodo[1])) + '\n'
	else:
		resp += 'Resultado: ' + ('Mensagem invalida') + '\n'
send_msg(resp)
tcp_ss.close()
