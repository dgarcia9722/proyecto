import time
import pygal
from pygal.style import LightStyle
from pymongo import MongoClient
import pprint
#import cairosvg

#client = MongoClient('mongodb://asalinas:RealNet2019@172.16.11.20:27017/registros')
client = MongoClient('mongodb://172.16.11.20:27017/')

db = client.registros
def functQuery(titulo,result,graph,nombre):
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)
        if element['_id'] == 'DNS':
            result.remove(element)
    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)


    if (len(result)>1):
        host = ['host', []]
        conteomb = ['mb', []]
        for i in range(len(result)):
            host[1].append(result[i]['_id'])
            conteomb[1].append(int(result[i]['total']))
        graph.title = titulo
        for i in range(9):
            graph.add(host[1][i], conteomb[1][i])
        graph_data = graph.render_to_png('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/templates/salidaReporte/archivos/tablas/'+nombre+'.png')
    return result


def functTable(result):
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)
        if element['_id'] == 'DNS':
            result.remove(element)
    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)
    return result

#TABLAS ANALISIS
def tb1_an(fechai,fechaf,empresa): #Top 10 categorias web
    graph = pygal.Pie(height=350)
    nombre = "an1"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.categoria","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    graph_data=functQuery("Top 10 web",result,graph,nombre)

    #pprint.pprint(graph_data)
    return graph_data


def tb2_an(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar(height=350)
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.Aplicacion","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    print("Aplicaciones")
    print(result)
    nombre = "an2"
    graph_data = functQuery("Top 10 aplicaciones",result,graph,nombre)
    return graph_data


def tb3_an(fechai,fechaf,empresa): #Top 10 usuarios bandwidth
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"user":"$_id.usuario","ip":"$_id.ip"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = functTable(result)

    return result

def tb4_an(fechai,fechaf,empresa):
    graph = pygal.Pie(height=350)
    result = db.virus.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$group":{"_id":{"fecha":"$_id.Fecha","hora":"$_id.hora","ip":"$_id.ip","usuario":"$_id.usuario","virus":"$_id.Virus","accion":"$_id.Accion","count":"$count"}}}
    ])
    result = list(result)
    return result


#TABLAS PRODUCTIVIDAD
def tb1_prod(fechai,fechaf,empresa): #Contenido adulto
    graph = pygal.Bar(height=350)
    nombre = "pd1"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":1},{"_id.uid":2},{"_id.uid":3}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.hostname","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])

    result = list(result)
    graph_data=functQuery("Contenido adulto",result,graph,nombre)
    return graph_data

def tb1u_prod(fechai,fechaf,empresa): #Usuarios contenido adulto
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":1},{"_id.uid":2},{"_id.uid":3}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"user":"$_id.usuario","ip":"$_id.ip"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = functTable(result)

    return result

def tb2_prod(fechai,fechaf,empresa): #Uso de datos
    graph = pygal.Pie(height=350)
    nombre = "pd2"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},
        {"$or":[{"_id.uid":4},{"_id.uid":5},{"_id.uid":6},{"_id.uid":7},{"_id.uid":8},{"_id.uid":73}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.hostname","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    graph_data=functQuery("Uso de datos",result,graph,nombre)

    #pprint.pprint(graph_data)
    return graph_data

def tb2u_prod(fechai,fechaf,empresa): #Usuarios contenido adulto
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":4},{"_id.uid":5},{"_id.uid":6},{"_id.uid":7},{"_id.uid":8},{"_id.uid":73}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"user":"$_id.usuario","ip":"$_id.ip"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = functTable(result)

    return result


def tb3_prod(fechai,fechaf,empresa): #Intereses personales
    graph = pygal.Pie(height=350)
    nombre = "pd3"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},{"_id.uid":{"$gte":9,"$lte":49}}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.hostname","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    graph_data=functQuery("Intereses personales",result,graph,nombre)
    print("Impresion")
    pprint.pprint(graph_data)
    return graph_data

def tb3u_prod(fechai,fechaf,empresa): #Usuarios contenido adulto
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},{"_id.uid":{"$gte":9,"$lte":49}}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"user":"$_id.usuario","ip":"$_id.ip"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = functTable(result)

    return result


def tb4_prod(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar(height=350)
    nombre = "pd4"
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},{"_id.uid":{"$gte":1,"$lte":7}}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": "$_id.Aplicacion","total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])

    result = list(result)
    print("Aplicaciones")
    pprint.pprint(result)
    graph_data = functQuery("Aplicaciones",result,graph,nombre)
    return graph_data

def tb4u_prod(fechai,fechaf,empresa): #Usuarios contenido adulto
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},{"_id.uid":{"$gte":1,"$lte":7}}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"user":"$_id.usuario","ip":"$_id.ip"},"total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = functTable(result)

    return result



#TABLAS RIESGOS LEGALES

def tb1_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    graph = pygal.Bar(height=350)
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":44},{"_id.uid":45},{"_id.uid":46},{"_id.uid":47},{"_id.uid":48},{"_id.uid":49},{"_id.uid":50},{"_id.uid":51},{"_id.uid":52}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    graph_data = functQuery("Sitios potencialmente problematicos",result,graph,nombre="rl1")
    return graph_data

def tb2_rl(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    graph = pygal.Bar(height=350)
    result = db.app.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":53},{"_id.uid":54},{"_id.uid":55},{"_id.uid":"Alternative Belifefs "},{"_id.uid":1},{"_id.uid":2},{"_id.uid":57},{"_id.uid":58},{"_id.uid":59},{"_id.uid":60},{"_id.uid":3},{"_id.uid":61},{"_id.uid":62},{"_id.uid":63},{"_id.uid":64}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    graph_data = functQuery("Contenido adulto",result,graph,nombre="rl1")
    return graph_data

def tb3_rl(fechai,fechaf,empresa): #Sitios de seguridad
    graph = pygal.Bar(height=350)
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":66},{"_id.uid":67},{"_id.uid":65}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    graph_data = functQuery("Riesgos de seguridad",result,graph,nombre="rl1")
    return graph_data

def tb4_rl(fechai,fechaf,empresa): #Sitios de seguridad
    graph = pygal.Bar(height=350)
    result = db.app.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":66},{"_id.uid":9},{"_id.uid":74},{"_id.uid":5},]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {" total": -1}},
        {"$limit":12}
    ])
    graph_data = functQuery("Top 10 aplicaciones",result,graph,nombre="rl1")
    return graph_data

#TABLAS FRAUDES
def tb1_fd(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},
        {"$or":[{"_id.uid":49},{"_id.uid":50},{"_id.uid":51},{"_id.uid":52}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    if result == None:
        result = 0
    pprint.pprint(result)




    return result

def tb2_fd(fechai,fechaf,empresa): #Sitios Adultos
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":1},{"_id.uid":2},{"_id.uid":64}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb3_fd(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":66},{"_id.uid":67},{"_id.uid":65},{"_id.uid":68},{"_id.uid":"Newly Observed Domain"},{"_id.uid":"Newly Registered Domain"}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb4_fd(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":9},{"_id.uid":11},{"_id.uid":"Brokearage and Trading "}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

def tb5_fd(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":72},{"_id.uid":71}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb6_fd(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.app.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.uid":5}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

#ROBO Y FUGA DE INFORMACION

def tb1_rf(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":49},{"_id.uid":52}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    if result == None:
        result = 0
    pprint.pprint(result)

    return result

def tb2_rf(fechai,fechaf,empresa): #Bandwidth
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":4},{"_id.uid":73},{"_id.uid":64}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb3_rf(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":66},{"_id.uid":67},{"_id.uid":65},{"_id.uid":68},{"_id.uid":"Newly Observed Domain"},{"_id.uid":"Newly Registered Domain"}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb4_rf(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":42},{"_id.uid":43}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb5_rf(fechai,fechaf,empresa): #Intereses de negocios
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":74},{"_id.uid":74},{"_id.uid":76},{"_id.uid":77}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb6_rf(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.app.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":11},{"_id.uid":8},{"_id.uid":9},{"_id.uid":12},{"_id.uid":5}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result
#LEALTAD
def tb1_ld(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":25},{"_id.uid":30},{"_id.uid":43}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)

    return result

def tb2_ld(fechai,fechaf,empresa): #Intereses de negocios
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":74},{"_id.uid":78},{"_id.uid":77}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

def tb3_ld(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.app.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":11},{"_id.uid":12},{"_id.uid":13}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result
##EVASION##
def tb1_ev(fechai,fechaf,empresa): #Sitios Potencialmente problematicos
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":49},{"_id.uid":52}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    if result == None:
        result = 0
    pprint.pprint(result)

    return result

def tb2_ev(fechai,fechaf,empresa): #Bandwidth
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":4},{"_id.uid":73},{"_id.uid":5}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

def tb3_ev(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":67},{"_id.uid":68},{"_id.uid":"Newly Observed Domain"},{"_id.uid":"Newly Registered Domain"}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

def tb4_ev(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":74}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
        ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

def tb5_ev(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":8},{"_id.uid":9},{"_id.uid":14},{"_id.uid":15},{"_id.uid":74},{"_id.uid":3},{"_id.uid":12},{"_id.uid":5}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

##BANDWIDTH

def tb1_bd(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":4},{"_id.uid":5},{"_id.uid":6},{"_id.uid":7},{"_id.uid":73},{"_id.uid":8}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result


def tb2_bd(fechai,fechaf,empresa): #Sitios de seguridad
    result = db.app.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":9},{"_id.uid":14},{"_id.uid":6},{"_id.uid":5}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Aplicacion":"$_id.Aplicacion"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result

#Revision de politicas
def tb1_ep(fechai,fechaf,empresa): #Intereses personales
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"$or":[{"_id.uid":66}]}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","Sitio":"$_id.hostname"}, "total":{"$sum":"$Total"}}},
        {"$sort": {"total": -1}}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] /2**20
    pprint.pprint(result)
    return result


initialDate = "2019-06-01"
finalDate = "2019-07-11"
empresa = "M-Movimiento"


start =time.time()
#envioCorreo(html)
#print("WEB")

#tb1_ep(initialDate, finalDate,empresa)
#tb2_bd(initialDate, finalDate,empresa)
#tb3_ev(initialDate, finalDate,empresa)
#tb4_ev(initialDate, finalDate,empresa)
#tb5_ev(initialDate, finalDate,empresa)
#tb6_rf(initialDate, finalDate,empresa)


print(time.time()-start)
