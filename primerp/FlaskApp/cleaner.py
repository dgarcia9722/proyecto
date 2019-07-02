from pymongo import MongoClient
import pygal
import time
import pprint
client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros

def lectorWeb(fechai,fechaf): #Top 10 paginas
    graph = pygal.Bar()
    print("MMMMMMMMMM")
    pipe3 = [
        {"$sort":{"date":1}},
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"subtype":"webfilter"}]}},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]},"Enviado":{"$sum":"$sentbyte"},"Recibido":{"$sum":"$rcvdbyte"}}},
        {"$group": {"_id":{"Empresa":"$devname","Fecha":"$date","categoria":"$catdesc","usuario":"$user","ip":"$srcip","hostname":"$hostname","Enviado":"$Enviado","Recibido":"$Recibido","Bytes":"$conteo"}}},
        {"$sort": {"Bytes": -1}},
    ]

    pipee = [
        {"$sort":{"date":1}},
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"subtype":"webfilter"}]}},
        {"$project":{"sentbyte":1,"rcvdbyte":1,"devname":1,"date":1,"catdesc":1,"user":1,"srcip":1,"hostname":1,"action":1,
        "punto":{"$switch":{
        "branches":[
        {'case':{'$eq':['$catdesc','Adult/Mature content ']},'then':1},
        {'case':{'$eq':['$catdesc','Dating ']},'then':1},
        {'case':{'$eq':['$catdesc','Gambling ']},'then':1},
        {'case':{'$eq':['$catdesc','Pornography ']},'then':1},
        {'case':{'$eq':['$catdesc','Bandwidth consuming ']},'then':1},
        {'case':{'$eq':['$catdesc','File Sharing and Storage ']},'then':1},
        {'case':{'$eq':['$catdesc','Freeware and Software Downloads ']},'then':1},
        {'case':{'$eq':['$catdesc','Internet Radio and TV ']},'then':1},
        {'case':{'$eq':['$catdesc','Internet Telephony ']},'then':1},
        {'case':{'$eq':['$catdesc','Peer to peer File Sharing ']},'then':1},
        {'case':{'$eq':['$catdesc','Streaming Media and Download  ']},'then':1},
        {'case':{'$eq':['$catdesc','General interest – Personal ']},'then':1},
        {'case':{'$eq':['$catdesc','Advertising ']},'then':1},
        {'case':{'$eq':['$catdesc','Arts and Culture ']},'then':1},
        {'case':{'$eq':['$catdesc','Auction ']},'then':1},
        {'case':{'$eq':['$catdesc','Brokerage and Trading ']},'then':1},
        {'case':{'$eq':['$catdesc','Child Education ']},'then':1},
        {'case':{'$eq':['$catdesc','Content Server ']},'then':1},
        {'case':{'$eq':['$catdesc','Digital Postcards ']},'then':1},
        {'case':{'$eq':['$catdesc','Domain Parking ']},'then':1},
        {'case':{'$eq':['$catdesc','Dynamic Content ']},'then':1},
        {'case':{'$eq':['$catdesc','Education ']},'then':1},
        {'case':{'$eq':['$catdesc','Entertaiment ']},'then':1},
        {'case':{'$eq':['$catdesc','Folklore ']},'then':1},
        {'case':{'$eq':['$catdesc','Games ']},'then':1},
        {'case':{'$eq':['$catdesc','Global Religion ']},'then':1},
        {'case':{'$eq':['$catdesc','Health and Wellnes ']},'then':1},
        {'case':{'$eq':['$catdesc','Instant Messaging ']},'then':1},
        {'case':{'$eq':['$catdesc','Job Search ']},'then':1},
        {'case':{'$eq':['$catdesc','Meaningless Content ']},'then':1},
        {'case':{'$eq':['$catdesc','Medicine ']},'then':1},
        {'case':{'$eq':['$catdesc','News and Media ']},'then':1},
        {'case':{'$eq':['$catdesc','Newsgroups and Message Boards ']},'then':1},
        {'case':{'$eq':['$catdesc','Personal Privacy ']},'then':1},
        {'case':{'$eq':['$catdesc','Personal Vehicles ']},'then':1},
        {'case':{'$eq':['$catdesc','Personal Websites and Blogs ']},'then':1},
        {'case':{'$eq':['$catdesc','Political Organizations ']},'then':1},
        {'case':{'$eq':['$catdesc','Real Estate ']},'then':1},
        {'case':{'$eq':['$catdesc','Reference ']},'then':1},
        {'case':{'$eq':['$catdesc','Restaurant and Dining ']},'then':1},
        {'case':{'$eq':['$catdesc','Shopping ']},'then':1},
        {'case':{'$eq':['$catdesc','Social Networking ']},'then':1},
        {'case':{'$eq':['$catdesc','Society and Lifestyles ']},'then':1},
        {'case':{'$eq':['$catdesc','Sports ']},'then':1},
        {'case':{'$eq':['$catdesc','Travel ']},'then':1},
        {'case':{'$eq':['$catdesc','Web Chat ']},'then':1},
        {'case':{'$eq':['$catdesc','Web-based Email ']},'then':1},
        {'case':{'$eq':['$catdesc','Potentially liable ']},'then':2},
        {'case':{'$eq':['$catdesc','Child Abuse ']},'then':2},
        {'case':{'$eq':['$catdesc','Discrimination ']},'then':2},
        {'case':{'$eq':['$catdesc','Drug Abuse ']},'then':2},
        {'case':{'$eq':['$catdesc','Explicit Violence ']},'then':2},
        {'case':{'$eq':['$catdesc','Extremist Groups ']},'then':2},
        {'case':{'$eq':['$catdesc','Hacking ']},'then':2},
        {'case':{'$eq':['$catdesc','Illegal or Unethical ']},'then':2},
        {'case':{'$eq':['$catdesc','Plagiarism ']},'then':2},
        {'case':{'$eq':['$catdesc','Proxy Avoidance ']},'then':2},
        {'case':{'$eq':['$catdesc','Adult/Mature content  ']},'then':2},
        {'case':{'$eq':['$catdesc','Abortion ']},'then':2},
        {'case':{'$eq':['$catdesc','Advocacy Organizations ']},'then':2},
        {'case':{'$eq':['$catdesc','Alcohol ']},'then':2},
        {'case':{'$eq':['$catdesc','Alternative Beliefs ']},'then':2},
        {'case':{'$eq':['$catdesc','Dating ']},'then':2},
        {'case':{'$eq':['$catdesc','Gambling ']},'then':2},
        {'case':{'$eq':['$catdesc','Lingerie and Swimsuit ']},'then':2},
        {'case':{'$eq':['$catdesc','Marijuana ']},'then':2},
        {'case':{'$eq':['$catdesc','Nudity and Risque ']},'then':2},
        {'case':{'$eq':['$catdesc','Other Adult Materials ']},'then':2},
        {'case':{'$eq':['$catdesc','Pornography ']},'then':2},
        {'case':{'$eq':['$catdesc','Sex Education ']},'then':2},
        {'case':{'$eq':['$catdesc','Sports Hunting and War Games ']},'then':2},
        {'case':{'$eq':['$catdesc','Tobacco ']},'then':2},
        {'case':{'$eq':['$catdesc','Weapons(Sales) ']},'then':2},
        {'case':{'$eq':['$catdesc','Security risk ']},'then':2},
        {'case':{'$eq':['$catdesc','Malicious websites ']},'then':2},
        {'case':{'$eq':['$catdesc','Phishing ']},'then':2},
        {'case':{'$eq':['$catdesc','Spam URLs ']},'then':2},
        {'case':{'$eq':['$catdesc','Potentially liable ']},'then':3},
        {'case':{'$eq':['$catdesc','Hacking  ']},'then':3},
        {'case':{'$eq':['$catdesc','Illegal or unethical ']},'then':3},
        {'case':{'$eq':['$catdesc','Plagiarism ']},'then':3},
        {'case':{'$eq':['$catdesc','Proxy avoidance ']},'then':3},
        {'case':{'$eq':['$catdesc','Adult/Mature content ']},'then':3},
        {'case':{'$eq':['$catdesc','Gambiling ']},'then':3},
        {'case':{'$eq':['$catdesc','Weapons (Sales) ']},'then':3},
        {'case':{'$eq':['$catdesc','Dating ']},'then':3},
        {'case':{'$eq':['$catdesc','Security risk ']},'then':3},
        {'case':{'$eq':['$catdesc','Dynamic DNS ']},'then':3},
        {'case':{'$eq':['$catdesc','Malicious Websites ']},'then':3},
        {'case':{'$eq':['$catdesc','Newly Observed Domain ']},'then':3},
        {'case':{'$eq':['$catdesc','Newly Registered Domain ']},'then':3},
        {'case':{'$eq':['$catdesc','Phishing ']},'then':3},
        {'case':{'$eq':['$catdesc','Spam URLs ']},'then':3},
        {'case':{'$eq':['$catdesc','General interest – Personal ']},'then':3},
        {'case':{'$eq':['$catdesc','Advertising ']},'then':3},
        {'case':{'$eq':['$catdesc','Auction ']},'then':3},
        {'case':{'$eq':['$catdesc','Brokearage and trading ']},'then':3},
        {'case':{'$eq':['$catdesc','Shopping ']},'then':3},
        {'case':{'$eq':['$catdesc','General interest – Business ']},'then':3},
        {'case':{'$eq':['$catdesc','Finance and banking ']},'then':3},
        {'case':{'$eq':['$catdesc','General organizations ']},'then':3},
        {'case':{'$eq':['$catdesc','Potentially liable ']},'then':4},
        {'case':{'$eq':['$catdesc','Hacking ']},'then':4},
        {'case':{'$eq':['$catdesc','Proxy avoidance ']},'then':4},
        {'case':{'$eq':['$catdesc','Bandwidth consuming ']},'then':4},
        {'case':{'$eq':['$catdesc','File sharing and storage ']},'then':4},
        {'case':{'$eq':['$catdesc','Peer-to-peer file sharing ']},'then':4},
        {'case':{'$eq':['$catdesc','Security risk ']},'then':4},
        {'case':{'$eq':['$catdesc','Dynamic DNS ']},'then':4},
        {'case':{'$eq':['$catdesc','Malicious Websites ']},'then':4},
        {'case':{'$eq':['$catdesc','Newly Observed Domain ']},'then':4},
        {'case':{'$eq':['$catdesc','Newly Registered Domain ']},'then':4},
        {'case':{'$eq':['$catdesc','Phishing ']},'then':4},
        {'case':{'$eq':['$catdesc','Spam URLs ']},'then':4},
        {'case':{'$eq':['$catdesc','General interest – Personal ']},'then':4},
        {'case':{'$eq':['$catdesc','Web chat ']},'then':4},
        {'case':{'$eq':['$catdesc','Web based email ']},'then':4},
        {'case':{'$eq':['$catdesc','General interest – Business ']},'then':4},
        {'case':{'$eq':['$catdesc','Online meeting ']},'then':4},
        {'case':{'$eq':['$catdesc','Remote Access ']},'then':4},
        {'case':{'$eq':['$catdesc','Web hosting ']},'then':4},
        {'case':{'$eq':['$catdesc','Web based applications ']},'then':4},
        {'case':{'$eq':['$catdesc','General interest – Personal ']},'then':5},
        {'case':{'$eq':['$catdesc','Job search ']},'then':5},
        {'case':{'$eq':['$catdesc','Personal privacy ']},'then':5},
        {'case':{'$eq':['$catdesc','Social Networking  ']},'then':5},
        {'case':{'$eq':['$catdesc','Linkedin ']},'then':5},
        {'case':{'$eq':['$catdesc','Web based email ']},'then':5},
        {'case':{'$eq':['$catdesc','General interest - Business ']},'then':5},
        {'case':{'$eq':['$catdesc','Business ']},'then':5},
        {'case':{'$eq':['$catdesc','Online meeting ']},'then':5},
        {'case':{'$eq':['$catdesc','Web based applications ']},'then':5},
        {'case':{'$eq':['$catdesc','Potentially liable ']},'then':6},
        {'case':{'$eq':['$catdesc','Hacking ']},'then':6},
        {'case':{'$eq':['$catdesc','Proxy avoidance ']},'then':6},
        {'case':{'$eq':['$catdesc','Bandwidth consuming ']},'then':6},
        {'case':{'$eq':['$catdesc','File sharing and storage ']},'then':6},
        {'case':{'$eq':['$catdesc','Freeware and software downloads ']},'then':6},
        {'case':{'$eq':['$catdesc','Peer to peer file sharing ']},'then':6},
        {'case':{'$eq':['$catdesc','Security Risk ']},'then':6},
        {'case':{'$eq':['$catdesc','Dynamic DNS ']},'then':6},
        {'case':{'$eq':['$catdesc','Newly observed domain ']},'then':6},
        {'case':{'$eq':['$catdesc','Newly registered domain ']},'then':6},
        {'case':{'$eq':['$catdesc','Spam URLs ']},'then':6},
        {'case':{'$eq':['$catdesc','Personal interest – Business ']},'then':6},
        {'case':{'$eq':['$catdesc','Remote access ']},'then':6},
        {'case':{'$eq':['$catdesc','Bandwidth consuming ']},'then':7},
        {'case':{'$eq':['$catdesc','File Sharing and Storage ']},'then':7},
        {'case':{'$eq':['$catdesc','Freeware and Software Downloads ']},'then':7},
        {'case':{'$eq':['$catdesc','Internet Radio and TV ']},'then':7},
        {'case':{'$eq':['$catdesc','Internet Telephony ']},'then':7},
        {'case':{'$eq':['$catdesc','Peer to peer File Sharing ']},'then':7},
        {'case':{'$eq':['$catdesc','Streaming Media and Download  ']},'then':7},

        ],
        "default":11
        }}
        }},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]},"Enviado":{"$sum":"$sentbyte"},"Recibido":{"$sum":"$rcvdbyte"}}},
        {"$group": {"_id":{"Empresa":"$devname","Fecha":"$date","categoria":"$catdesc","usuario":"$user","ip":"$srcip","hostname":"$hostname","Accion":"$action","Enviado":"$Enviado","Recibido":"$Recibido","Bytes":"$conteo","Punto":"$punto"}}},
        {"$sort": {"Fecha": -1}},
        #{"$out":"pruebaweb"},
    ]
    result = db.logs.aggregate(pipee,allowDiskUse=True)
    #result = list(result)
    #print(result)
    for element in result:
        #pprint.pprint(element)
        db.web.insert_one(element)
    print("Listo")

def lectorApp(fechai,fechaf): #Top 10 paginas
    print("MMMMMMMMMM")
    pipee = [
        {"$sort":{"date":1}},
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"subtype":"app-ctrl"}]}},
        {"$project":{"sentbyte":1,"rcvdbyte":1,"devname":1,"date":1,"appcat":1,"user":1,"srcip":1,"app":1,"action":1,
        "punto":{"$switch":{
        "branches":[
        {'case':{'$eq':['$appcat','Mobile ']},'then':1},
        {'case':{'$eq':['$appcat','Game ']},'then':1},
        {'case':{'$eq':['$appcat','Web client ']},'then':1},
        {'case':{'$eq':['$appcat','General Interest ']},'then':1},
        {'case':{'$eq':['$appcat','P2P ']},'then':1},
        {'case':{'$eq':['$appcat','Social Media ']},'then':1},
        {'case':{'$eq':['$appcat','Video/Audio ']},'then':1},
        {'case':{'$eq':['$appcat','Proxy ']},'then':2},
        {'case':{'$eq':['$appcat','Storage backup ']},'then':2},
        {'case':{'$eq':['$appcat','Remote access ']},'then':2},
        {'case':{'$eq':['$appcat','P2P ']},'then':2},
        {'case':{'$eq':['$appcat','P2P ']},'then':3},
        {'case':{'$eq':['$appcat','Email ']},'then':4},
        {'case':{'$eq':['$appcat','Proxy ']},'then':4},
        {'case':{'$eq':['$appcat','Storage backup ']},'then':4},
        {'case':{'$eq':['$appcat','Collaboration ']},'then':4},
        {'case':{'$eq':['$appcat','P2P ']},'then':4},
        {'case':{'$eq':['$appcat','Business ']},'then':5},
        {'case':{'$eq':['$appcat','Email ']},'then':5},
        {'case':{'$eq':['$appcat','Collaboration ']},'then':5},
        {'case':{'$eq':['$appcat','Proxy ']},'then':6},
        {'case':{'$eq':['$appcat','Storage backup ']},'then':6},
        {'case':{'$eq':['$appcat','Cloud IT ']},'then':6},
        {'case':{'$eq':['$appcat','Network service ']},'then':6},
        {'case':{'$eq':['$appcat','Remote access ']},'then':6},
        {'case':{'$eq':['$appcat','Web client ']},'then':6},
        {'case':{'$eq':['$appcat','Collaboration ']},'then':6},
        {'case':{'$eq':['$appcat','P2P ']},'then':6},
        {'case':{'$eq':['$appcat','Storage backup ']},'then':7},
        {'case':{'$eq':['$appcat','P2P ']},'then':7},
        {'case':{'$eq':['$appcat','Social media ']},'then':7},
        {'case':{'$eq':['$appcat','Video/Audio ']},'then':7},
        ],
        "default":11
        }}
        }},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]},"Enviado":{"$sum":"$sentbyte"},"Recibido":{"$sum":"$rcvdbyte"}}},
        {"$group": {"_id":{"Empresa":"$devname","Fecha":"$date","Punto":"$punto","categoria":"$appcat","Aplicacion":"$app","usuario":"$user","ip":"$srcip","Accion":"$action","Enviado":"$Enviado","Recibido":"$Recibido","Bytes":"$conteo"}}},
        {"$sort": {"Bytes": -1}},
        {"$out":"aplicacion"},
    ]
    result = db.logs.aggregate(pipee,allowDiskUse=True)
    #for element in result:
        #pprint.pprint(element)
    #    db.aplicacion.insert_one(element)
    print("Listo")

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
