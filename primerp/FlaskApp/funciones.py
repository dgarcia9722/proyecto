import pygal
from pymongo import MongoClient


def graph_1():
    client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
    db = client.prueba
    graph = pygal.Bar()
    result = db.logsprueba.aggregate([{"$group": {"_id": "$catdesc", "count": {"$sum": 1}}}, {"$sort": {"_id": -1}}])
    numero = ['numero ', []]
    conteo = ['conteo ', []]
    for doc in result:
        numero[1].append(doc['_id'])
        conteo[1].append(int(doc['count']))
    graph.title = 'Grafica de prueba'
    for i in range(10):
        graph.add(numero[1][i], conteo[1][i])
    graph_data = graph.render_data_uri()
    return graph_data


