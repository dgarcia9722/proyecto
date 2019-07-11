import threading
import time
import os

f = open('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/lp.log','r',encoding='latin-1') #Carga del archivo
c =1
nv = "abc"+str(c)


def acumulador(n):
    #global abc+(str(c))
    #abc1 = 1
    #abc+str(c) = abc+str(c)+n
    print("dsadsa")


def prueba():
    while 1:
        global entrada
        print("La entrada es:")
        print(entrada)
        time.sleep(2)

#thread = threading.Thread(target=prueba)
thread = threading.Thread(target=acumulador,args=[1])
thread2 = threading.Thread(target=acumulador,args=[2])

thread.start()
thread2.start()

print(abc+str(c))
#thread.start()
