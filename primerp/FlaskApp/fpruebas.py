import time
import pygal
from pygal.style import Style
from pymongo import MongoClient
import pprint
from pygal.style import DarkStyle
#import cairosvg

client = MongoClient('mongodb://172.16.11.20:27017/')

db = client.registros
def functQuery1(titulo,result,graph,nombre,ptotal):
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)
        if element['_id'] == 'DNS':
            result.remove(element)
    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)
        element['recibido'] = element['recibido'] / 2**20
        element['recibido'] = round(element['recibido'],2)
        element['enviado'] = element['enviado'] / 2**20
        element['enviado'] = round(element['enviado'],2)
    ptotal = ptotal / 2**20
    print("porcentaje total: "+str(ptotal))

    if (len(result)>1):
        host = ['app', []]
        conteomb = ['mb', []]
        for i in range(len(result)):
            pelement = (int(result[i]['total'])) * 100 / ptotal
            pelement = round(pelement,2)
            host[1].append(result[i]['_id'] +" "+str(pelement)+"%")
            conteomb[1].append(int(result[i]['total']))
        graph.title = titulo
        for i in range(len(result)):
            graph.add(host[1][i], conteomb[1][i])
        graph_data = graph.render_to_png('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/templates/salidaReporte/archivos/tablas/'+nombre+'.png')
    pprint.pprint(result)

    return result

def functQuery(titulo,result,graph,nombre,ptotal):
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)
        if element['_id'] == 'DNS':
            result.remove(element)
    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)
        element['recibido'] = element['recibido'] / 2**20
        element['recibido'] = round(element['recibido'],2)
        element['enviado'] = element['enviado'] / 2**20
        element['enviado'] = round(element['enviado'],2)
    ptotal = ptotal / 2**20
    if (len(result)>1):
        host = ['app', []]
        conteomb = ['mb', []]
        for i in range(len(result)):
            pelement = (int(result[i]['total'])) * 100 / ptotal
            pelement = round(pelement,2)
            host[1].append(result[i]['_id'] +" "+str(pelement)+"%")
            #host[1].append(result[i]['_id'])
            #conteomb[1].append(int(result[i]['total']))
            conteomb[1].append(pelement)
            #conteomb[1].append(int(result[i]['total']))
        graph.title = titulo
        for i in range(len(result)):
            graph.add(host[1][i], conteomb[1][i])
        graph_data = graph.render_to_png('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/templates/salidaReporte/archivos/tablas/'+nombre+'.png')
    pprint.pprint(result)

    return result


def functQueryApp(titulo,result,graph,nombre,ptotal):
    result = list(result)

    for element in result:
        if not 'App' in element['_id']:
            result.remove(element)
    for element in result:
        if not 'App' in element['_id']:
            result.remove(element)

    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)
        element['recibido'] = element['recibido'] / 2**20
        element['recibido'] = round(element['recibido'],2)
        element['enviado'] = element['enviado'] / 2**20
        element['enviado'] = round(element['enviado'],2)
    ptotal = ptotal / 2**20

    if (len(result)>1):
        host = ['host', []]
        conteomb = ['mb', []]
        for i in range(len(result)):
            pelement = (int(result[i]['total'])) * 100 / ptotal
            pelement = round(pelement,2)
            host[1].append(result[i]['_id']['App'] +" "+str(pelement)+"%")
#            host[1].append(result[i]['_id']['App'])
            #conteomb[1].append(int(result[i]['total']))
            #conteomb[1].append(int(result[i]['total']))
            conteomb[1].append(pelement)
        graph.title = titulo
        for i in range(len(result)):
            graph.add(host[1][i], conteomb[1][i])
        graph_data = graph.render_to_png('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/templates/salidaReporte/archivos/tablas/'+nombre+'.png')
    return result

def functQueryUsuarios(titulo,result,graph,nombre,ptotal):
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)
        if element['_id'] == 'DNS':
            result.remove(element)

    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)
        element['recibido'] = element['recibido'] / 2**20
        element['recibido'] = round(element['recibido'],2)
        element['enviado'] = element['enviado'] / 2**20
        element['enviado'] = round(element['enviado'],2)
    ptotal = ptotal / 2**20
    if (len(result)>1):
        host = ['app', []]
        conteomb = ['mb', []]
        for i in range(len(result)):
            pelement = (int(result[i]['total'])) * 100 / ptotal
            pelement = round(pelement,2)
            host[1].append(result[i]['_id']['ip'] +" "+str(pelement)+"%")
            #conteomb[1].append(int(result[i]['total']))
            #conteomb[1].append(int(result[i]['total']))
            conteomb[1].append(pelement)
            #conteomb[1].append(pelement)
        graph.title = titulo
        for i in range(len(result)):
            graph.add(host[1][i], conteomb[1][i])
        graph_data = graph.render_to_png('C:/Users/asalinas/Documents/PycharmProjects/flask/proyecto/primerp/primerp/FlaskApp/templates/salidaReporte/archivos/tablas/'+nombre+'.png')
    pprint.pprint(result)

    return result

############## FUNCIONES REPORTES #############################


miStyle = Style(
  background='white',
  plot_background='white',
  )

def rep1(fechai,fechaf,empresa): #Top 10 categorias web
    graph = pygal.Pie(height=500,fill=True, interpolate='cubic',legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6,style=miStyle)
    nombre = "rep1"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": "$_id.categoria","total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
    print(ptotal)

    graph_data=functQuery1("Sitios web",result,graph,nombre,ptotal)
    pprint.pprint(graph_data)
    return graph_data

def rep2(fechai,fechaf,empresa): #Top usuarios categorias web
    graph = pygal.Pie(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep2"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","hostname":"$_id.hostname",'categoria':'$_id.categoria',},"total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
    graph_data=functQueryUsuarios("Usuarios",result,graph,nombre,ptotal)
    pprint.pprint(graph_data)
    return result



def rep3(fechai,fechaf,empresa): #Usuarios Wifi
    graph = pygal.Pie(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep3"
    result = db.appwifi.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {'usuario':'$_id.usuario',"ip":"$_id.ip","hostname":"$_id.hostname","SSID":"$_id.SSID"},"total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
#    result = list(result)
#    for element in result:
#        element['total'] = element['total'] / 2**20
#        element['total'] = round(element['total'],2)
#        element['enviado'] = element['enviado'] / 2**20
#        element['enviado'] = round(element['enviado'],2)
#        element['recibido'] = element['recibido'] / 2**20
#        element['recibido'] = round(element['recibido'],2)
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
    graph_data=functQueryUsuarios("Usuarios",result,graph,nombre,ptotal)

    pprint.pprint(result)
    return result

def rep4(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep4"
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"App":"$_id.Aplicacion","Categoria":"$_id.categoria"}, "total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    print("Resultado")
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
        #pprint.pprint(len(result))
    graph_data = functQueryApp("Aplicaciones",result,graph,nombre,ptotal)

    return graph_data

def rep5(fechai,fechaf,empresa): #Top 10 Audio/Video
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep5"
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.uid":7}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"App":"$_id.Aplicacion","Categoria":"$_id.categoria"}, "total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
        ])
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']

    graph_data=functQueryApp("Audio y video",result,graph,nombre,ptotal)
    return graph_data

def rep6(fechai,fechaf,empresa): #Top 10 Audio/Video por usuario
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)

    nombre = "rep6"
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.uid":7}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"App":"$_id.Aplicacion","Usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria"}, "total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])

    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']

    graph_data=functQueryUsuarios("Audio y video por usuario",result,graph,nombre,ptotal)
    return graph_data

def rep7(fechai,fechaf,empresa): #Top 10 Audio/Video WIFI por usuario
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep7"
    result = db.appwifi.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.uid":7}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"Usuario":"$_id.usuario","ip":"$_id.ip","Categoria":"$_id.categoria","SSID":"$_id.SSID"}, "total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']

    graph_data=functQueryUsuarios("Audio y video por WIFI",result,graph,nombre,ptotal)
#    print(graph_data)
    return graph_data

def rep8(fechai,fechaf,empresa): #Sitios web permitidos
    graph = pygal.Bar(height=600,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=1,legend_box_size=6)
    nombre = "rep8"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.Accion":"passthrough"}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": "$_id.hostname","total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']

    graph_data=functQuery("Sitios permitidos",result,graph,nombre,ptotal)
    return graph_data


def rep9(fechai,fechaf,empresa): #Categorias web bloqueadas
    graph = pygal.Pie(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep9"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},{"_id.Accion":"blocked"}]}},
        {"$group": {"_id": "$_id.categoria","total":{"$sum":1}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)

    pprint.pprint(result)
    #graph_data=functQuery("Categorias bloqueadas",result,graph,nombre)
    #pprint.pprint(graph_data)
    return result

def rep10(fechai,fechaf,empresa): #Sitios web bloqueados
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep10"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.Accion":"blocked"}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {'hostname':"$_id.hostname",'categoria':"$_id.categoria"},"total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    for element in result:
        if element['_id'] == None:
            result.remove(element)

    pprint.pprint(result)

    #graph_data=functQuery("Sitios web bloqueados",result,graph,nombre)
    return result

def rep11(fechai,fechaf,empresa): #Top usuarios categorias web bloqueados
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep11"
    result = db.web.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte":fechai, "$lte":fechaf}},{"_id.Empresa":empresa},{"_id.Accion":"blocked"}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"usuario":"$_id.usuario","ip":"$_id.ip","categoria":"$_id.categoria"},"total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    result = list(result)
    for element in result:
        element['total'] = element['total'] / 2**20
        element['total'] = round(element['total'],2)
        element['recibido'] = element['recibido'] / 2**20
        element['recibido'] = round(element['recibido'],2)
        element['enviado'] = element['enviado'] / 2**20
        element['enviado'] = round(element['enviado'],2)

    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
    #graph_data=functQuery("Usuarios",result,graph,nombre)
    #pprint.pprint(graph_data)
    return result

def rep12(fechai,fechaf,empresa):
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep12"
    result = db.virus.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa}]}},
        {"$group":{"_id":{"fecha":"$_id.Fecha","usuario":"$_id.usuario","ip":"$_id.ip","virus":"$_id.Virus","Accion":"$_id.Accion","count":"$count"}}}
    ])
    result = list(result)

    pprint.pprint(result)
    return result

def rep13(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep13"
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.categoria":'Proxy'}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"App":"$_id.Aplicacion","Categoria":"$_id.categoria"}, "total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    print("Resultado")
    result = list(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
        #pprint.pprint(len(result))
    graph_data = functQueryApp("Aplicaciones",result,graph,nombre,ptotal)

    return graph_data
def rep14(fechai,fechaf,empresa): #Top 10 aplicaciones
    graph = pygal.Bar(height=500,fill=True, interpolate='cubic', style=miStyle,legend_at_bottom=True,legend_at_bottom_columns=2,legend_box_size=6)
    nombre = "rep14"
    result = db.aplicacion.aggregate([
        {"$match": {"$and": [{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}},{"_id.Empresa": empresa},{"_id.categoria":'Social.Media'}]}},
        {"$addFields":{"Total": {"$sum":"$_id.Bytes"},"Enviado": {"$sum":"$_id.Enviado"},"Recibido": {"$sum":"$_id.Recibido"}}},
        {"$group": {"_id": {"App":"$_id.Aplicacion"}, "total":{"$sum":"$Total"},"enviado":{"$sum":"$Enviado"},"recibido":{"$sum":"$Recibido"}}},
        {"$sort": {"total": -1}},
        {"$limit":12}
    ])
    print("Resultado")
    result = list(result)
    pprint.pprint(result)
    ptotal=0
    for element in result:
        ptotal = ptotal+element['total']
        #pprint.pprint(len(result))
    graph_data = functQueryApp("Aplicaciones",result,graph,nombre,ptotal)

    return graph_data




start =time.time()

initialDate = '2019-06-07'
finalDate = '2019-08-07'
empresa = "TLA HA 1"

#consulta = rep5(initialDate,finalDate,empresa)
consulta = rep14(initialDate,finalDate,empresa)
pprint.pprint(consulta)

print(time.time()-start)
