import pygal
from pygal.style import LightStyle
from pymongo import MongoClient


client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.registros
def functQuery(titulo,result,graph):
    result = list(result)

    if (len(result)>1):
        if result[0] == 'DNS':
            n1 = result[0]
        else:
            n1 = result[1]
        numero = ['numero ', []]
        conteo = ['conteo ', []]
        appunk = []
        for doc in result:
            if (doc['_id']==None):
                doc['_id']='Desconocido'
            if 'Desconocido' in doc['_id']:
                appunk.append(doc)
            else:
                if "DNS" in doc['_id']:
                    pass;
                else:
                    numero[1].append(doc['_id'])
                    conteo[1].append(int(doc['count']))
        graph.title = titulo
        for i in range(10):
            graph.add(numero[1][i], conteo[1][i])
        graph_data = graph.render_data_uri()
        return graph_data,appunk,n1

#TABLAS PRODUCTIVIDAD
def graph_1(fechai,fechaf,empresa): #Top 10 categorias web
    graph = pygal.Bar()
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        #{"$project":{"catdesc":{"$ifNull":["$catdesc","Desconocido"]}}},
        {"$group": {"_id": "$catdesc", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    graph_data=functQuery("Top 10 web",result,graph)
    return graph_data


def tb1_prod(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar()
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        #{"$project":{"app":{"$ifNull":["$app","Desconocido"]}}},
        {"$group": {"_id": "$app", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    graph_data = functQuery("Top 10 aplicaciones",result,graph)
    return graph_data


def tb3_prod(fechai,fechaf,empresa): #Top 10 paginas
    graph = pygal.Bar()
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        #{"$project":{"hostname":{"$ifNull":["$hostname","Desconocido"]}}},
        {"$group": {"_id": "$hostname", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    graph_data = functQuery("Top 10 sitios web",result,graph)
    return graph_data

def tb4_prod(fechai,fechaf,empresa): #Top 10 bandwidth
    graph = pygal.Bar()
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        {"$addFields":{"count": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": "$hostname","count":{"$sum": "$sentbyte"}}},
        {"$sort": {"count": -1}}
    ])
    result = list(result)
    #print(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    print(result[0])

    graph_data = functQuery("Top 10 sitios bandwidth",result,graph)
    return graph_data

#TABLAS RIESGOS LEGALES
def tb1_rl(fechai,fechaf,empresa): #Top 10 bandwidth
    graph = pygal.Bar()
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        {"$addFields":{"count": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": "$hostname","count":{"$sum": "$sentbyte"}}},
        {"$sort": {"count": -1}}
    ])
    result = list(result)
    #print(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    print(result[0])

    graph_data = functQuery("Top 10 sitios bandwidth",result,graph)
    return graph_data
