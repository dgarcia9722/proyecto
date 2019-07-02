from pymongo import MongoClient
import pygal
import time
import pprint
client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros

def prueba(fechai,fechaf,empresa): #Top 10 paginas
    graph = pygal.Bar()
    print("MMMMMMMMMM")
    graph = pygal.Bar()
    pipee = [

        {"$match": {"$and": [{"_id.Empresa": empresa},{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}}]}},
        {"$group": {"_id": "$_id.categoria", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]
    result = db.pruebas.aggregate(pipee,allowDiskUse=True)

    result = list(result)
    pprint.pprint(result)

#var fechai = "2019-06-01"
#var fechaf = "2019-08-01"

initialDate = "2018-06-24"
finalDate = "2020-07-01"
empresa = 'HA-RNT FG100D'

start =time.time()

#resultado2 = lectorWeb (initialDate, finalDate)
resultado2 = lectorApp(initialDate, finalDate)

print(time.time()-start)
