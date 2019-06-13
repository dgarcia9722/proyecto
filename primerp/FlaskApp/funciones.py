import pygal
from pygal.style import LightStyle
from pymongo import MongoClient
import pprint


client = MongoClient('mongodb://asalinas:RealNet2019@172.16.11.20:27017/registros')
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

def tb4_prod(fechai,fechaf,empresa): #Top 10 bandwidth web
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa},{"subtype":"webfilter"}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": "$hostname","count":{"$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    for element in result:
        if element['_id'] == None:
            element['_id'] = 'Desconocida'
        element['conteo'] = element['conteo'] /1024
    return result
def tb5_prod(fechai,fechaf,empresa): #Top 10 bandwidth app
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": "$app","count":{ "$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    #print(result[0])

    for element in result:
        if element['_id'] == None:
            element['_id'] = 'Desconocida'
        element['conteo'] = element['conteo'] /1024
    return result

def tb6_prod(fechai,fechaf,empresa): #Top 10 usuarios bandwidth
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip"},"count":{ "$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    print("HOLA")
    print(result)

    for element in result:
        if element['_id'] == None:
            element['_id'] = 'No registrado'
        element['conteo'] = element['conteo'] /1024
    print(result)

    return result



#TABLAS RIESGOS LEGALES

def tb1_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa},{"$or":[    {"catdesc":"Child Abuse "},{"catdesc":"Discrimination "},{"catdesc":"Drug Abuse "},{"catdesc":"Explicit Violence "},{"catdesc":"Extremist Groups "},{"catdesc":"Hacking "},{"catdesc":"Illegal or Unethical "},{"catdesc":"Plagiarism "},{"catdesc":"Proxy Avoidance "}]}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip","Categoria":"$catdesc","Sitio":"$hostname"},"count":{ "$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    pprint.pprint(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    return result

def tb2_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa},{"$or":[    {"catdesc":"Abortion "},{"catdesc":"Advocacy Organizations "},{"catdesc":"Alcohol "},{"catdesc":"Alternative Belifefs "},{"catdesc":"Dating "},{"catdesc":"Gambling "},{"catdesc":"Lingerie and Swimsuit "},{"catdesc":"Marijuana "},{"catdesc":"Nudity and Risque "},{"catdesc":"Other Adult Materials "},{"catdesc":"Pornography "},{"catdesc":"Sex Education "},{"catdesc":"Sports Hunting and War Games "},{"catdesc":"Tobacco "},{"catdesc":"Weapons(Sales) "}]}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip","Categoria":"$catdesc","Sitio":"$hostname"},"count":{ "$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    return result

def tb3_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa},{"$or":[{"catdesc":"Phishing "},{"catdesc":"Spam URLs "},{"catdesc":"Malicious websites "}]}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip","Categoria":"$catdesc","Sitio":"$hostname"},"count":{ "$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    return result
