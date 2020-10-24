import numpy as np
import socket
import time

ClientMultiSocket = socket.socket()

#conecta com o servidor
host = '127.0.0.4'
port = 2007
ClientMultiSocket.connect((host, port))

#assim que conectado ele recebe um sinal que esta conctado
res = ClientMultiSocket.recv(1024)

#cria minha matriz que sera utilizada como exemplo da funcionalidade
list1 = np.random.randint(low=1, high=2, size=(10, 10))

#variavel pra controlar se a matriz ja foi somada
rodar = 1
while True:
    if rodar == 1:

        #sem threads (st significa SEM-THREAD)
        soma_total_st = 0
        tempo_total_st = 0

        #contador de tempo de execucao
        start2 = time.time()

        #loop pra somar minha matriz sem thread
        for i in list1:
            #somo cada liha da matriz e adiciono na minha variavel soma_total_st
            soma_total_st = soma_total_st + int(i.sum())

        #finalizado o for paro de contar o tempo e realizo a subtracao
        end2 = time.time()
        tempo_total_st = tempo_total_st + (end2 - start2)

        #com threads
        soma_total = 0
        tempo_total = 0

        print('Waiting for connection response')
        try:
            start = time.time()
            for i in list1:
                #envio cada linha da minha matriz pra meu servidor (de forma criptografada)
                ClientMultiSocket.send(str(i).encode())

                #recebo a soma
                res = ClientMultiSocket.recv(1024)

                #adiciono no meu total
                soma_total = soma_total + int(res)

            end = time.time()

            tempo_total = tempo_total + (end - start)
            rodar = 0

            print("Soma st: " + str(soma_total_st))
            print("Soma:    " + str(soma_total))

            print("Tempo st: " + str(tempo_total_st))
            print("Tempo:    " + str(tempo_total))

        except socket.error as e:
            print(str(e))

ClientMultiSocket.close()
