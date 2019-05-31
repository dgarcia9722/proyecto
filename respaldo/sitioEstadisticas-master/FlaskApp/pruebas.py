from pymongo import MongoClient

import json
import pygal

client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.prueba
result = db.logsprueba.aggregate([
    {"$group":{"_id": "$catdesc","count":{"$sum":1}}},
    {"$sort":{"_id":-1}}
])
print(list(result))

#numero = ['numero ', []]
#conteo = ['conteo ', []]
#for doc in result:
 #   numero[1].append(int(doc['_id']))
  #  conteo[1].append(int(doc['count']))
#print(conteo[1][0])
#print(numero[1][0])

#print(conteo[1][2])
#print(numero[1][2])

#<!--{%for elemento in consulta%}
 #   <p>numero: {{elemento._id}}</p>
  #  <p>#: {{elemento.count}}</p>
#{%endfor%}
#-->

#<p>Consulta aparte: </p>
#<!--{{consulta[0]._id}}-->


