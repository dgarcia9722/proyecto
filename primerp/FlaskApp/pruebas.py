from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from pymongo import MongoClient

client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros
dempresa = db.empresas.find()
dempresa = list(dempresa)
fecha = dempresa[0]['inicio']

fechan = datetime.strptime(fecha,'%Y-%m-%d')
fechahoy = datetime.now()

diccionario = {"sentbyte":10,"rcvdbyte":None}
if diccionario.get("sentbyte")==None:
    print("Bien")
else:
    diccionario['sentbyte'] = 11



print(diccionario.get("sentbyte"))
