import pymongo


cliente = pymongo.MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["registros"]
coleccion = mydb["logs"]

infoempresa = mydb.empresas.find_one({"devname":'TLA HA 1'})
print(infoempresa['contacto'][0][0])
