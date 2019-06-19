##### HOLA #######
import os
import time
import re
import pymongo
import ast
import json
from notificaciones import *

cliente = pymongo.MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["registros"]
coleccion = mydb["logs"]

f = open('/run/media/root/sda3/FG/172.16.11.27.log','r',encoding='latin-1') #Carga del archivo

def follow(f): #Funcion que lee el ultimo renglon del archivo, si detecta cambios espera 0.3 segundos para volver a correr
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            #time.sleep(0.1)
            continue
        yield line


loglines = follow(f)


for data in loglines:
#    print(data)
   # s = re.findall('"(.*?)"', data)
    #for i in range(len(s)):
     #   texto = s[i].replace(":", " ")
      #  data = data.replace(s[i], texto)

    s = re.findall('"(.*?)"', data)
    for i in range(len(s)):
        texto = s[i].replace(" ","_")
 #       print(texto)
  #      print(s[i])
        data = data.replace('"'+s[i]+'"', texto)
   #     print(data)

    s = re.findall('"(.*?)"', data)
    for i in range(len(s)):
        texto = s[i].replace("=", "==")
        data = data.replace(s[i], texto)

    data = data.replace('"','')
    data = data.split(" ")
    full_data = []
    diccionario = {}
    x = []
#    print(data)
    for e in data:
        full_data.append(e.split("="))
    for e in range (4,len(full_data)):
        full_data[e][0] = full_data[e][0].replace('.',' ')

        if full_data[e][0]=='sentbyte':
#            valor = "{'"+full_data[e][0]+"':"+full_data[e][1]+"}"
            valor = '{"'+full_data[e][0]+'":'+full_data[e][1]+'}'
        else:

            if full_data[e][0]=='rcvdbyte':
#                valor = "{'"+full_data[e][0]+"':"+full_data[e][1]+"}"
                valor = '{"'+full_data[e][0]+'":'+full_data[e][1]+'}'
            else:
#                valor = "{'"+full_data[e][0]+"':'"+full_data[e][1]+"'}"
                valor = '{"'+full_data[e][0]+'":"'+full_data[e][1]+'"}'
        valor = valor.replace('\n',' ')
        valor = valor.replace('_',' ')
        #valor = valor.replace('.',' ')
        vcast = ast.literal_eval(valor)
        diccionario.update(vcast)
#    print(diccionario)
    qdict = ['logver','timestamp','tz','devid','vd','logtime','policyid','sessionid','srcintf','srcintfrole','dstintf','dstintfrole','proto','profile','reqtype','direction','method','cat','cookies','itime','vdid','xauthuser','group','xauthgroup','remport','locport','itime_t','outintf','sentdelta','rcvddelta','dstserver','wanin','wanout','lanin','lanout','countweb','countapp','crscore','craction','srcssid','apsn','ap','channel','radioband']

    for q in qdict:
        try:
            diccionario.pop(q)
        except:
            pass

#    if diccionario.get('catdesc') == 'Web-based Email ':
 #       print(diccionario.get('catdesc'))
    seleccion(diccionario)
    insercion = coleccion.insert_one(diccionario)
f.close()

#@
