import pprint
from pymongo import MongoClient
import json
import pygal
import pprint
client = MongoClient('mongodb://localhost:27017')
db = client.registros


#diccionario = [
#{"Ingles":["Hello","Goodbye"]},
#{"Español":["Hola","Adios"]},
#]
#print(diccionario[0]["Ingles"]["Hello"])
fechai = "2018-01-01"
fechaf = "2020-01-01"
empresa = "FWF90D3Z13000359"

result = db.logs.aggregate([
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"devname": empresa},{"$or":[    {"catdesc":"Abortion "},{"catdesc":"Advocacy Organizations "},{"catdesc":"Alcohol "},{"catdesc":"Alternative Belifefs "},{"catdesc":"Dating "},{"catdesc":"Gambling "},{"catdesc":"Lingerie and Swimsuit "},{"catdesc":"Marijuana "},{"catdesc":"Nudity and Risque "},{"catdesc":"Other Adult Materials "},{"catdesc":"Pornography "},{"catdesc":"Sex Education "},{"catdesc":"Sports Hunting and War Games "},{"catdesc":"Tobacco "},{"catdesc":"Weapons(Sales) "}]}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]}}},
        {"$group": {"_id": {"usuario":"$user","ip":"$srcip","Categoria":"$catdesc","Sitio":"$hostname"},"count":{ "$sum": "$sentbyte"},"conteo":{"$sum":"$conteo"}}},
        {"$sort": {"conteo": -1}}
    ])
result = list(result)
pprint.pprint(len(result))

for elemnt in result:
    elemnt['count'] = elemnt['count'] /1024
pprint.pprint(result)