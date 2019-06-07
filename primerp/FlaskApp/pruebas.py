import pprint
from pymongo import MongoClient
import json
import pygal

#client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
#db = client.prueba
#{"$match": {"date": fecha}},
#    {"$match":{"$and":[{"$gt":["date",fechai],"$lt":["date",fechaf]}]}},

#fechai = "2012-05-23";fechaf = "2012-05-29";
#result = db.logsprueba.aggregate([
 #       {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}}]}},
  #      {"$group": {"_id": "$catdesc", "count": {"$sum": 1}}},
   #     {"$sort": {"_id": -1}}
   # ])

#result = db.logsprueba.aggregate([
 #       {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}}]}},
  #      {"$group": {"_id": "$catdesc", "count:": {"$sum": 1}}}
   # ])

#result = db.logsprueba.aggregate([
 #   {"$match":{"$and":[{"date":{"$gte":fechai,"$lte":fechaf}},{"catdesc":"Business"}]}},
  #  {"$group":{"_id":"$catdesc","Conteo:":{"$sum":1}}}
#])
#result = db.logsprueba.aggregate([{"$match":{"date":fechai}}])

#pprint.pprint(len(list(result)))


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

#result = db.logsprueba.aggregate([{"$group": {"_id": "$catdesc", "count": {"$sum": 1}}}, {"$sort": {"_id": -1}}])

#{"$group":{"_id": "$catdesc","count":{"$sum":1}}},
 #   {"$sort":{"_id":-{1}}

#resultado = db.logsprueba.aggregate([{"$match":{"date":fechai}},{"$group": {"_id": "$catdesc", "count": {"$sum": 1}}}, {"$sort": {"_id": -1}}])


import pygal
from pymongo import MongoClient


client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.registros
graph = pygal.Bar()
#result = db.logsprueba.aggregate([{"$group": {"_id": "$catdesc", "count": {"$sum": 1}}}, {"$sort": {"_id": -1}}])

fechai = "2017-05-23"
fechaf = "2020-05-29"
devname = "FWFRNT"

result = db.logs.aggregate([
    {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}}]}},
    {"$group": {"_id": {"devname":"$devname","categoria":"$catdesc"}, "count": {"$sum": 1}}},
    {"$sort": {"_id": -1}}
])
resultados = list(result)
print(len(resultados))
#pprint.pprint(resultados)
#pprint.pprint(resultados[1])



def graph_1(fechai,fechaf,empresa):
    graph = pygal.Bar()
    #result = db.logsprueba.aggregate([{"$group": {"_id": "$catdesc", "count": {"$sum": 1}}}, {"$sort": {"_id": -1}}])
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        {"$group": {"_id": "$catdesc", "count": {"$sum": 1}}},
        {"$sort": {"_id": -1}}
    ])
    result = list(result)
    if (len(result)>1):
        numero = ['numero ', []]
        conteo = ['conteo ', []]
        for doc in result:
            numero[1].append(doc['_id'])
            conteo[1].append(int(doc['count']))
        graph.title = 'Grafica de prueba'
        #print("Prueba")
        print(len(numero[1]))
        for i in range(10):
            graph.add(numero[1][i], conteo[1][i])
        graph_data = graph.render_data_uri()
        return graph_data
data = graph_1(fechai,fechaf,devname)

empresa = "FWFRNT"
resulta = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}}]}},
        {"$group": {"_id": {"categoria:":"$catdesc","dispositivo":"$devname"}, "count": {"$sum": 1}}},
        {"$sort": {"_id": -1}}
    ])
resulta = list(resulta)

pprint.pprint(resulta)
