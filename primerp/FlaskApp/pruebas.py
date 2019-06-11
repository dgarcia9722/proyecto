import pprint
from pymongo import MongoClient
import json
import pygal
client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.registros


#diccionario = [
#{"Ingles":["Hello","Goodbye"]},
#{"Español":["Hola","Adios"]},
#]
#print(diccionario[0]["Ingles"]["Hello"])
fechai = "2018-01-01"
fechaf = "2020-01-01"
empresa = "Allan"
result = db.logs.aggregate([
    {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa}]}},
    {"$addFields":{"count": {"$sum":["$sentbyte","$rcvdbyte"]}}},
    {"$group": {"_id": "$hostname","count":{"$sum": "$sentbyte"}}},
    {"$sort": {"count": -1}}
])


result = list(result)
print(result)
