import socket
from _thread import *
import numpy as np

#criando socket
ServerSideSocket = socket.socket()
host = '127.0.0.4'
port = 2007
ThreadCount = 0

#conectando socket a porta
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))

    while True:

        #recebe o array
        data = connection.recv(2048)

        #realiza a soma de todos os dados(numpy array) recebidos
        result1 = int(((np.fromstring(data[1:-1], sep=' ').astype(int)).sum()))

        if not data:
            break

        #envia a soma de volta pro cliente
        connection.sendall(str(result1).encode())

    connection.close()

#loop que torda o servidor sempre disponivel pra toda solicitacao
while True:
    #sempre aceita uma coneccao
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))

    #comeca uma nova thread pra esse novo cliente conectado
    start_new_thread(multi_threaded_client, (Client, ))

    #conta quantos clientes esetao conectados
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()