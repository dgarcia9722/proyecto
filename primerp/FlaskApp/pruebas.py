from pymongo import MongoClient
import pygal
import time
import pprint
client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros

def functQuery(titulo,result,graph):
    result = list(result)
    pprint.pprint(result)
    if (len(result)>1):
        host = ['host', []]
        conteomb = ['mb', []]
        for i in range(9):
            host[1].append(result[i]['_id'])
            conteomb[1].append(int(result[i]['total']))
        graph.title = titulo
        for i in range(9):
            graph.add(host[1][i], conteomb[1][i])

        #graph_data = graph.render_data_uri()
        #graph_data = graph.render_to_file('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/templates/salidaReporte/archivos/chart.svg')
        #return graph_data
    print("BIEN")

#TABLAS PRODUCTIVIDAD
def graph_1(fechai,fechaf,empresa): #Top 10 categorias web
    graph = pygal.Bar()
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.categoria","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":10}
    ])
    pprint.pprint(result)
    graph_data=functQuery("Top 10 web",result,graph)
    return graph_data


def tb1_prod(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar()
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.Aplicacion","total":{"$sum":"$Total"},"count": {"$sum": 1},}},
        {"$sort": {"count": -1}},
        {"$limit":10}
    ])
    pprint.pprint(result)

    graph_data = functQuery("Top 10 aplicaciones",result,graph)

    return graph_data


def tb3_prod(fechai,fechaf,empresa): #Top 10 paginas
    graph = pygal.Bar()
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.hostname","total":{"$sum":"$Total"},"count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit":10}
    ])
    pprint.pprint(result)

    graph_data = functQuery("Top 10 sitios web",result,graph)
    return graph_data

def tb4_prod(fechai,fechaf,empresa): #Top 10 bandwidth web
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.hostname","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":10}
    ])
    result = list(result)

    for element in result:
        element['total'] = element['total'] /2**20

    pprint.pprint(result)

    return result

def tb5_prod(fechai,fechaf,empresa): #Top 10 bandwidth app
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.Aplicacion","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":10}
    ])
    result = list(result)
    print("KHEEEEEEEEE")
    pprint.pprint(result)

    for element in result:
        element['total'] = element['total'] /2**20
#    pprint.pprint(result)

    return result

def tb6_prod(fechai,fechaf,empresa): #Top 10 usuarios bandwidth
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"user":"$_id.Usuario","ip":"$_id.ip"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":10}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

#TABLAS RIESGOS LEGALES

def tb1_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.webp.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":44},{"_id.uid":45},{"_id.uid":46},{"_id.uid":47},{"_id.uid":48},{"_id.uid":49},{"_id.uid":50},{"_id.uid":51},{"_id.uid":52}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    #pprint.pprint(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    print(result)
    return result

def tb2_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.webp.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":53},{"_id.uid":54},{"_id.uid":55},{"_id.uid":56},{"_id.uid":1},
        {"_id.uid":2},{"_id.uid":57},{"_id.uid":58},{"_id.uid":59},{"_id.uid":59},{"_id.uid":3},{"_id.uid":61},{"_id.uid":62},{"_id.uid":63},{"_id.uid":64}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip","Categoria":"$catdesc","Sitio":"$_id.hostname"},"count":{ "$sum": "$sentbyte"},"total":{"$sum":"$Total"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    print(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    return result

def tb3_rl(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.webp.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":65},{"_id.uid":66},{"_id.uid":67}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip","Categoria":"$catdesc","Sitio":"$_id.hostname"},"count":{ "$sum": "$sentbyte"},"total":{"$sum":"$Total"}}},
        {"$sort": {"conteo": -1}}
    ])
    result = list(result)
    print(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    return result

def tb4_rl(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":9},{"_id.uid":10},{"_id.uid":5},]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Aplicacion":"$_id.Aplicacion","Categoria":"$_id.Categoria",},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    pprint.pprint(result)
    for elemnt in result:
        elemnt['count'] = elemnt['count'] /1024
    return result

###FRAUDES###
def tb1_fd(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.logs.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"$_id.uid":49},{"$_id.uid":50},{"$_id.uid":51},{"$_id.uid":52}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['total'] = elemnt['total'] /1024

    return result

def tb2_fd(fechai,fechaf,empresa): #Sitios Adultos
    result = db.logs.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"$_id.uid":1},{"$_id.uid":2},{"$_id.uid":64}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['total'] = elemnt['total'] /1024
    return result

def tb3_fd(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.logs.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"$_id.uid":66},{"$_id.uid":67},{"$_id.uid":65},{"$_id.uid":68},{"$_id.uid":69},{"$_id.uid":70}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['total'] = elemnt['total'] /1024
    return result

def tb4_fd(fechai,fechaf,empresa): #Intereses personales
    result = db.logs.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"$_id.uid":"Advertising "},{"$_id.uid":"Auction "},{"$_id.uid":"Brokearage and Trading "}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['total'] = elemnt['total'] /1024
    print(result)
    return result

def tb5_fd(fechai,fechaf,empresa): #Intereses personales
    result = db.logs.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"$_id.uid":"General Organizations "},{"$_id.uid":"Finance and Banking "}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['total'] = elemnt['total'] /1024
    return result

def tb6_fd(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.logs.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.uid":"P2P "}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.Aplicacioncat","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for elemnt in result:
        elemnt['total'] = elemnt['total'] /1024
    return result

initialDate = "2019-01-25"
finalDate = "2019-07-02"
empresa = 'HA-RNT FG100D'

start =time.time()

#resultado2 = lectorWeb (initialDate, finalDate)
print("WEB")
resultado2 = tb4_rl(initialDate, finalDate,empresa)


print(time.time()-start)
