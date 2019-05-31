from pymongo import MongoClient
import pprint

import json
import pygal

client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.prueba
#{"$match": {"date": fecha}},
#    {"$match":{"$and":[{"$gt":["date",fechai],"$lt":["date",fechaf]}]}},

fechai = "2019-05-22";fechaf = "2019-05-29";

result = db.logsprueba.aggregate([
    {"$match":{"$and":[{"date":{"$gte":fechai,"$lte":fechaf}},{"catdesc":"Business"}]}},
    {"$group":{"_id":"$catdesc","Conteo:":{"$sum":1}}}
])
resultado = db.logsprueba.aggregate([
    {"$match":{"$and":[{"$match":{"$and":[{"date":{"$gte":fechai,"$lte":fechaf}},{"catdesc":"Business"}]}},
             {"$match":{"$and":[{"date":{"$gte":fechai,"$lte":fechaf}},{"catdesc":"Social Networking"}]}}
             ]}},
    {"$group":{"_id":"$catdesc","Conteo:":{"$sum":1}}}
])

pprint.pprint(list(resultado))


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



#{"$group":{"_id": "$catdesc","count":{"$sum":1}}},
 #   {"$sort":{"_id":-{1}}