import os
import time
import time
import pprint
import threading
import queue

tiempo = 0

f = open('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/lp.log','r',encoding='latin-1') #Carga del archivo

class objetoAcumulador(object):
    def __init__(self,nombre,conteo):
        self.nombre = nombre
        self.conteo = conteo



def follow(f): #Funcion que lee el ultimo renglon del archivo, si detecta cambios espera 0.3 segundos para volver a correr
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            #time.sleep(0.1)
            continue
        yield line
        #return line
def lector(loglines):
    global linea
    global cola
    cola = queue.Queue()

    objetoNotificacion = objetoAcumulador('Allan',0)
    print(objetoNotificacion.nombre)
    for line in loglines:
        if line != "\n":
            linea = line
            cola.put(linea)
            if linea == objetoNotificacion.nombre:
                objetoNotificacion.conteo += 1
                texto ='nombre: {} y conteo: {}'.format(objetoNotificacion.nombre,objetoNotificacion.conteo)
                print(texto)
            else:

            if  objetoNotificacion.conteo > 3:
                 objetoNotificacion.conteo = 0
                 objetoNotificacion.nombre = 'Joshua'
                 while not cola.empty():
                    print(cola.get())


def temporizador():
    global tiempo
    tiempo = time.time()
    while 1:
        tfinal = time.time()-tiempo
        if tfinal > 5:
            print("Tiempo alcanzado")
            print(tfinal)
            break
    print(time.time()-start)

start = time.time()
x = []
loglines = follow(f)
lector(loglines)

colaacum = queue.Queue()
colad = queue.Queue()

hilo1 = threading.Thread(target=temporizador)
hilo1.start()

acumulador = 0
for i in range(5):
    dato = input()
    dato = int(dato)
    if dato == acumulador:
        print("iguales")
        colad.put(dato)
        tiempo = time.time()
    else:
        colaacum.put(dato)

print("Cola acumulador")
while not colaacum.empty():
    print(colaacum.get())
print("Cola datos")
while not colad.empty():
    print(colad.get())
#Hola soy Diana
