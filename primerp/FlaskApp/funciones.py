import pygal
from pymongo import MongoClient

client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.registros

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
        for i in range(len(numero[1])):
            graph.add(numero[1][i], conteo[1][i])
        graph_data = graph.render_data_uri()
        return graph_data







