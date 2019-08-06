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
        #{"$match": {"$and": [{"date":fechai},{"subtype":"webfilter"}]}},
        {"$project":{"sentbyte":1,"rcvdbyte":1,"devname":1,"date":1,"catdesc":1,"user":1,"srcip":1,"hostname":1,"action":1,"duration":1,
        "punto":{"$switch":{
        "branches":[
        {'case':{'$eq':['$catdesc','Adult/Mature content ']},'then':[1,2,3]},
        {'case':{'$eq':['$catdesc','Dating ']},'then':[1,2,3]},
        {'case':{'$eq':['$catdesc','Gambling ']},'then':[1,2,3]},
        {'case':{'$eq':['$catdesc','Pornography ']},'then':[1,2]},
        {'case':{'$eq':['$catdesc','Bandwidth consuming ']},'then':[1,4,6,7]},
        {'case':{'$eq':['$catdesc','File Sharing and Storage ']},'then':[1,4,6,7]},
        {'case':{'$eq':['$catdesc','Freeware and Software Downloads ']},'then':[1,6,7]},
        {'case':{'$eq':['$catdesc','Internet Radio and TV ']},'then':[1,7]},
        {'case':{'$eq':['$catdesc','Internet Telephony ']},'then':[1,7]},
        {'case':{'$eq':['$catdesc','Peer to peer File Sharing ']},'then':[1,6,7]},
        {'case':{'$eq':['$catdesc','Streaming Media and Download  ']},'then':[1,7]},
        {'case':{'$eq':['$catdesc','General interest – Personal ']},'then':[1,3,4,5]},
        {'case':{'$eq':['$catdesc','Advertising ']},'then':[1,3]},
        {'case':{'$eq':['$catdesc','Arts and Culture ']},'then':1},
        {'case':{'$eq':['$catdesc','Auction ']},'then':[1,3]},
        {'case':{'$eq':['$catdesc','Brokerage and Trading ']},'then':[1,3]},
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
        {'case':{'$eq':['$catdesc','Health and Wellness ']},'then':1},
        {'case':{'$eq':['$catdesc','Instant Messaging ']},'then':1},
        {'case':{'$eq':['$catdesc','Job Search ']},'then':[1,5]},
        {'case':{'$eq':['$catdesc','Meaningless Content ']},'then':1},
        {'case':{'$eq':['$catdesc','Medicine ']},'then':1},
        {'case':{'$eq':['$catdesc','News and Media ']},'then':1},
        {'case':{'$eq':['$catdesc','Newsgroups and Message Boards ']},'then':1},
        {'case':{'$eq':['$catdesc','Personal Privacy ']},'then':[1,5]},
        {'case':{'$eq':['$catdesc','Personal Vehicles ']},'then':1},
        {'case':{'$eq':['$catdesc','Personal Websites and Blogs ']},'then':1},
        {'case':{'$eq':['$catdesc','Political Organizations ']},'then':1},
        {'case':{'$eq':['$catdesc','Real Estate ']},'then':1},
        {'case':{'$eq':['$catdesc','Reference ']},'then':1},
        {'case':{'$eq':['$catdesc','Restaurant and Dining ']},'then':1},
        {'case':{'$eq':['$catdesc','Shopping ']},'then':[1,3]},
        {'case':{'$eq':['$catdesc','Social Networking ']},'then':[1,5]},
        {'case':{'$eq':['$catdesc','Society and Lifestyles ']},'then':1},
        {'case':{'$eq':['$catdesc','Sports ']},'then':1},
        {'case':{'$eq':['$catdesc','Travel ']},'then':1},
        {'case':{'$eq':['$catdesc','Web Chat ']},'then':[1,4]},
        {'case':{'$eq':['$catdesc','Web-based Email ']},'then':1},
        {'case':{'$eq':['$catdesc','Potentially liable ']},'then':[2,3,4,6]},
        {'case':{'$eq':['$catdesc','Child Abuse ']},'then':2},
        {'case':{'$eq':['$catdesc','Discrimination ']},'then':2},
        {'case':{'$eq':['$catdesc','Drug Abuse ']},'then':2},
        {'case':{'$eq':['$catdesc','Explicit Violence ']},'then':2},
        {'case':{'$eq':['$catdesc','Extremist Groups ']},'then':2},
        {'case':{'$eq':['$catdesc','Hacking ']},'then':[2,3,4,6]},
        {'case':{'$eq':['$catdesc','Illegal or Unethical ']},'then':2},
        {'case':{'$eq':['$catdesc','Plagiarism ']},'then':[2,3]},
        {'case':{'$eq':['$catdesc','Proxy Avoidance ']},'then':[2,3,4,6]},
        {'case':{'$eq':['$catdesc','Abortion ']},'then':2},
        {'case':{'$eq':['$catdesc','Advocacy Organizations ']},'then':2},
        {'case':{'$eq':['$catdesc','Alcohol ']},'then':2},
        {'case':{'$eq':['$catdesc','Alternative Beliefs ']},'then':2},
        {'case':{'$eq':['$catdesc','Lingerie and Swimsuit ']},'then':2},
        {'case':{'$eq':['$catdesc','Marijuana ']},'then':2},
        {'case':{'$eq':['$catdesc','Nudity and Risque ']},'then':2},
        {'case':{'$eq':['$catdesc','Other Adult Materials ']},'then':2},
        {'case':{'$eq':['$catdesc','Sex Education ']},'then':2},
        {'case':{'$eq':['$catdesc','Sports Hunting and War Games ']},'then':2},
        {'case':{'$eq':['$catdesc','Tobacco ']},'then':2},
        {'case':{'$eq':['$catdesc','Weapons(Sales) ']},'then':[2,3]},
        {'case':{'$eq':['$catdesc','Security risk ']},'then':[2,3,4,6]},
        {'case':{'$eq':['$catdesc','Malicious websites ']},'then':[2,3,4]},
        {'case':{'$eq':['$catdesc','Phishing ']},'then':[2,3,4]},
        {'case':{'$eq':['$catdesc','Spam URLs ']},'then':[2,3,4,6]},
        {'case':{'$eq':['$catdesc','Dynamic DNS ']},'then':[3,4,6]},
        {'case':{'$eq':['$catdesc','Newly Observed Domain ']},'then':[3,4,6]},
        {'case':{'$eq':['$catdesc','Newly Registered Domain ']},'then':[3,4,6]},
        {'case':{'$eq':['$catdesc','General interest – Business ']},'then':[3,4,5,6]},
        {'case':{'$eq':['$catdesc','Finance and banking ']},'then':3},
        {'case':{'$eq':['$catdesc','General organizations ']},'then':3},
        {'case':{'$eq':['$catdesc','Peer-to-peer file sharing ']},'then':4},
        {'case':{'$eq':['$catdesc','Web based email ']},'then':[4,5]},
        {'case':{'$eq':['$catdesc','Online meeting ']},'then':[4,5]},
        {'case':{'$eq':['$catdesc','Remote Access ']},'then':[4,6]},
        {'case':{'$eq':['$catdesc','Web hosting ']},'then':4},
        {'case':{'$eq':['$catdesc','Web based applications ']},'then':4},
        {'case':{'$eq':['$catdesc','Business ']},'then':5},
        {'case':{'$eq':['$catdesc','Web based applications ']},'then':5},

        ],
        "default":11
        }},
        "uid":{"$switch":{
        "branches":[
        {'case':{'$eq':['$catdesc','Dating ']},'then':1},
        {'case':{'$eq':['$catdesc','Gambling ']},'then':2},
        {'case':{'$eq':['$catdesc','Pornography ']},'then':3},
        {'case':{'$eq':['$catdesc','File Sharing and Storage ']},'then':4},
        {'case':{'$eq':['$catdesc','Freeware and Software Downloads ']},'then':5},
        {'case':{'$eq':['$catdesc','Internet Radio and TV ']},'then':6},
        {'case':{'$eq':['$catdesc','Internet Telephony ']},'then':7},
        {'case':{'$eq':['$catdesc','Streaming Media and Download ']},'then':8},
        {'case':{'$eq':['$catdesc','Advertising ']},'then':9},
        {'case':{'$eq':['$catdesc','Arts and Culture ']},'then':10},
        {'case':{'$eq':['$catdesc','Auction ']},'then':11},
        {'case':{'$eq':['$catdesc','Brokerage and Trading ']},'then':12},
        {'case':{'$eq':['$catdesc','Child Education ']},'then':13},
        {'case':{'$eq':['$catdesc','Content Servers ']},'then':14},
        {'case':{'$eq':['$catdesc','Digital Postcards ']},'then':15},
        {'case':{'$eq':['$catdesc','Domain Parking ']},'then':16},
        {'case':{'$eq':['$catdesc','Dynamic Content ']},'then':17},
        {'case':{'$eq':['$catdesc','Education ']},'then':18},
        {'case':{'$eq':['$catdesc','Entertaiment ']},'then':19},
        {'case':{'$eq':['$catdesc','Folklore ']},'then':20},
        {'case':{'$eq':['$catdesc','Games ']},'then':21},
        {'case':{'$eq':['$catdesc','Global Religion ']},'then':22},
        {'case':{'$eq':['$catdesc','Health and Wellness ']},'then':23},
        {'case':{'$eq':['$catdesc','Instant Messaging ']},'then':24},
        {'case':{'$eq':['$catdesc','Job Search ']},'then':25},
        {'case':{'$eq':['$catdesc','Meaningless Content ']},'then':26},
        {'case':{'$eq':['$catdesc','Medicine ']},'then':27},
        {'case':{'$eq':['$catdesc','News and Media ']},'then':28},
        {'case':{'$eq':['$catdesc','Newsgroups and Message Boards ']},'then':29},
        {'case':{'$eq':['$catdesc','Personal Privacy ']},'then':30},
        {'case':{'$eq':['$catdesc','Personal Vehicles ']},'then':31},
        {'case':{'$eq':['$catdesc','Personal Websites and Blogs ']},'then':32},
        {'case':{'$eq':['$catdesc','Political Organizations ']},'then':33},
        {'case':{'$eq':['$catdesc','Real Estate ']},'then':34},
        {'case':{'$eq':['$catdesc','Reference ']},'then':35},
        {'case':{'$eq':['$catdesc','Restaurant and Dining ']},'then':36},
        {'case':{'$eq':['$catdesc','Shopping ']},'then':37},
        {'case':{'$eq':['$catdesc','Social Networking ']},'then':38},
        {'case':{'$eq':['$catdesc','Society and Lifestyles ']},'then':39},
        {'case':{'$eq':['$catdesc','Sports ']},'then':40},
        {'case':{'$eq':['$catdesc','Travel ']},'then':41},
        {'case':{'$eq':['$catdesc','Web Chat ']},'then':42},
        {'case':{'$eq':['$catdesc','Web-based Email ']},'then':43},
        {'case':{'$eq':['$catdesc','Child Abuse ']},'then':44},
        {'case':{'$eq':['$catdesc','Discrimination ']},'then':45},
        {'case':{'$eq':['$catdesc','Drug Abuse ']},'then':46},
        {'case':{'$eq':['$catdesc','Explicit Violence ']},'then':47},
        {'case':{'$eq':['$catdesc','Extremist Groups ']},'then':48},
        {'case':{'$eq':['$catdesc','Hacking ']},'then':49},
        {'case':{'$eq':['$catdesc','Illegal or Unethical ']},'then':50},
        {'case':{'$eq':['$catdesc','Plagiarism ']},'then':51},
        {'case':{'$eq':['$catdesc','Proxy Avoidance ']},'then':52},
        {'case':{'$eq':['$catdesc','Abortion ']},'then':53},
        {'case':{'$eq':['$catdesc','Advocacy Organizations ']},'then':54},
        {'case':{'$eq':['$catdesc','Alcohol ']},'then':55},
        {'case':{'$eq':['$catdesc','Alternative Beliefs ']},'then':56},
        {'case':{'$eq':['$catdesc','Lingerie and Swimsuit ']},'then':57},
        {'case':{'$eq':['$catdesc','Marijuana ']},'then':58},
        {'case':{'$eq':['$catdesc','Nudity and Risque ']},'then':59},
        {'case':{'$eq':['$catdesc','Other Adult Materials ']},'then':60},
        {'case':{'$eq':['$catdesc','Sex Education ']},'then':61},
        {'case':{'$eq':['$catdesc','Sports Hunting and War Games ']},'then':62},
        {'case':{'$eq':['$catdesc','Tobacco ']},'then':63},
        {'case':{'$eq':['$catdesc','Weapons(Sales) ']},'then':64},
        {'case':{'$eq':['$catdesc','Malicious websites ']},'then':65},
        {'case':{'$eq':['$catdesc','Phishing ']},'then':66},
        {'case':{'$eq':['$catdesc','Spam URLs ']},'then':67},
        {'case':{'$eq':['$catdesc','Dynamic DNS ']},'then':68},
        {'case':{'$eq':['$catdesc','Newly Observed Domain ']},'then':69},
        {'case':{'$eq':['$catdesc','Newly Registered Domain ']},'then':70},
        {'case':{'$eq':['$catdesc','Finance and banking ']},'then':71},
        {'case':{'$eq':['$catdesc','General organizations ']},'then':72},
        {'case':{'$eq':['$catdesc','Peer-to-peer file sharing ']},'then':73},
        {'case':{'$eq':['$catdesc','Online meeting ']},'then':74},
        {'case':{'$eq':['$catdesc','Remote Access ']},'then':75},
        {'case':{'$eq':['$catdesc','Web hosting ']},'then':76},
        {'case':{'$eq':['$catdesc','Web-based applications ']},'then':77},
        {'case':{'$eq':['$catdesc','Business ']},'then':78},
        ],
        "default":0
        }},
        }},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]},"Enviado":{"$sum":"$sentbyte"},"Recibido":{"$sum":"$rcvdbyte"}}},
        {"$group": {"_id":{"Fecha":"$date","Empresa":"$devname","uid":"$uid","Punto":"$punto","categoria":"$catdesc","usuario":"$user","ip":"$srcip","hostname":"$hostname","Accion":"$action","Enviado":"$Enviado","Recibido":"$Recibido","Bytes":"$conteo","Duracion":{"$sum":"$duration"}}}},
        {"$sort": {"Fecha": -1}},
        {"$out":"web"},
    ]
    db.logs.aggregate(pipee,allowDiskUse=True)
    #result = list(result)
    #print(result)
    #
    #for element in result:
        #pprint.pprint(element)
    #    db.web.insert_one(element)
    print("Listo")

def lectorApp(fechai,fechaf): #Top 10 paginas
    print("MMMMMMMMMM")
    pipee = [
        {"$sort":{"date":1}},
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"subtype":"forward"}]}},
        #{"$match": {"$and": [{"date":fechai},{"subtype":"forward"}]}},
        {"$project":{"sentbyte":1,"rcvdbyte":1,"devname":1,"date":1,"appcat":1,"user":1,"srcip":1,"app":1,"action":1,"duration":1,"appcat":1,
        "punto":{"$switch":{
        "branches":[
        {'case':{'$eq':['$appcat','Mobile']},'then':1},
        {'case':{'$eq':['$appcat','Game']},'then':1},
        {'case':{'$eq':['$appcat','Web client']},'then':[1,6]},
        {'case':{'$eq':['$appcat','General Interest']},'then':1},
        {'case':{'$eq':['$appcat','P2P']},'then':[1,2,3,4,6,7]},
        {'case':{'$eq':['$appcat','Social Media']},'then':[1,7]},
        {'case':{'$eq':['$appcat','Video/Audio']},'then':[1,7]},
        {'case':{'$eq':['$appcat','Proxy']},'then':[2,4,6]},
        {'case':{'$eq':['$appcat','Storage backup']},'then':[2,4,6,7]},
        {'case':{'$eq':['$appcat','Remote access']},'then':[2,6]},
        {'case':{'$eq':['$appcat','Email']},'then':[4,5]},
        {'case':{'$eq':['$appcat','Collaboration']},'then':[4,5,6]},
        {'case':{'$eq':['$appcat','Business']},'then':5},
        {'case':{'$eq':['$appcat','Cloud IT']},'then':6},
        {'case':{'$eq':['$appcat','Network service']},'then':6},
        ],
        "default":11
        }},
        "uid":{"$switch":{
        "branches":[
        {'case':{'$eq':['$appcat','Mobile']},'then':1},
        {'case':{'$eq':['$appcat','Game']},'then':2},
        {'case':{'$eq':['$appcat','Web client']},'then':3},
        {'case':{'$eq':['$appcat','General Interest']},'then':4},
        {'case':{'$eq':['$appcat','P2P']},'then':5},
        {'case':{'$eq':['$appcat','Social Media']},'then':6},
        {'case':{'$eq':['$appcat','Video/Audio']},'then':7},
        {'case':{'$eq':['$appcat','Proxy']},'then':8},
        {'case':{'$eq':['$appcat','Storage backup']},'then':9},
        {'case':{'$eq':['$appcat','Remote access']},'then':10},
        {'case':{'$eq':['$appcat','Email']},'then':11},
        {'case':{'$eq':['$appcat','Collaboration']},'then':12},
        {'case':{'$eq':['$appcat','Business']},'then':13},
        {'case':{'$eq':['$appcat','Cloud IT']},'then':14},
        {'case':{'$eq':['$appcat','Network service']},'then':15},
        ],
        "default":11
        }}

        }},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]},"Enviado":{"$sum":"$sentbyte"},"Recibido":{"$sum":"$rcvdbyte"},"Duracion":{"$sum":"$duration"}}},
        {"$group": {"_id":{"Fecha":"$date","Empresa":"$devname","uid":"$uid","Punto":"$punto","categoria":"$appcat","Aplicacion":"$app","usuario":"$user","ip":"$srcip","Accion":"$action","Enviado":"$Enviado","Recibido":"$Recibido","Bytes":"$conteo","Duracion":"$Duracion"}}},
        {"$sort": {"Empresa": -1}},
        {"$out":"aplicacion"},
    ]
    db.logs.aggregate(pipee,allowDiskUse=True)
    result = list(result)
    print(result)
#    for element in result:
        #pprint.pprint(element)
#        db.aplicacion.insert_one(element)
    print("Listo")

def lectorAppWifi(fechai,fechaf): #Top 10 paginas
    print("MMMMMMMMMM")
    pipee = [
        {"$sort":{"date":1}},
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"subtype":"forward"},{"srcssid":{"$exists":True}}]}},
        #{"$match": {"$and": [{"date":fechai},{"subtype":"forward"}]}},
        {"$project":{"srcssid":1,"sentbyte":1,"rcvdbyte":1,"devname":1,"date":1,"appcat":1,"user":1,"srcip":1,"app":1,"action":1,"duration":1,"appcat":1,
        "punto":{"$switch":{
        "branches":[
        {'case':{'$eq':['$appcat','Mobile']},'then':1},
        {'case':{'$eq':['$appcat','Game']},'then':1},
        {'case':{'$eq':['$appcat','Web client']},'then':[1,6]},
        {'case':{'$eq':['$appcat','General Interest']},'then':1},
        {'case':{'$eq':['$appcat','P2P']},'then':[1,2,3,4,6,7]},
        {'case':{'$eq':['$appcat','Social Media']},'then':[1,7]},
        {'case':{'$eq':['$appcat','Video/Audio']},'then':[1,7]},
        {'case':{'$eq':['$appcat','Proxy']},'then':[2,4,6]},
        {'case':{'$eq':['$appcat','Storage backup']},'then':[2,4,6,7]},
        {'case':{'$eq':['$appcat','Remote access']},'then':[2,6]},
        {'case':{'$eq':['$appcat','Email']},'then':[4,5]},
        {'case':{'$eq':['$appcat','Collaboration']},'then':[4,5,6]},
        {'case':{'$eq':['$appcat','Business']},'then':5},
        {'case':{'$eq':['$appcat','Cloud IT']},'then':6},
        {'case':{'$eq':['$appcat','Network service']},'then':6},
        ],
        "default":11
        }},
        "uid":{"$switch":{
        "branches":[
        {'case':{'$eq':['$appcat','Mobile']},'then':1},
        {'case':{'$eq':['$appcat','Game']},'then':2},
        {'case':{'$eq':['$appcat','Web client']},'then':3},
        {'case':{'$eq':['$appcat','General Interest']},'then':4},
        {'case':{'$eq':['$appcat','P2P']},'then':5},
        {'case':{'$eq':['$appcat','Social Media']},'then':6},
        {'case':{'$eq':['$appcat','Video/Audio']},'then':7},
        {'case':{'$eq':['$appcat','Proxy']},'then':8},
        {'case':{'$eq':['$appcat','Storage backup']},'then':9},
        {'case':{'$eq':['$appcat','Remote access']},'then':10},
        {'case':{'$eq':['$appcat','Email']},'then':11},
        {'case':{'$eq':['$appcat','Collaboration']},'then':12},
        {'case':{'$eq':['$appcat','Business']},'then':13},
        {'case':{'$eq':['$appcat','Cloud IT']},'then':14},
        {'case':{'$eq':['$appcat','Network service']},'then':15},
        ],
        "default":11
        }}

        }},
        {"$addFields":{"conteo": {"$sum":["$sentbyte","$rcvdbyte"]},"Enviado":{"$sum":"$sentbyte"},"Recibido":{"$sum":"$rcvdbyte"},"Duracion":{"$sum":"$duration"}}},
        {"$group": {"_id":{"Fecha":"$date","Empresa":"$devname","uid":"$uid","Punto":"$punto","categoria":"$appcat","Aplicacion":"$app","usuario":"$user","ip":"$srcip","SSID":"$srcssid","Accion":"$action","Enviado":"$Enviado","Recibido":"$Recibido","Bytes":"$conteo","Duracion":"$Duracion"}}},
        {"$sort": {"Empresa": -1}},
        {"$out":"appwifi"},
    ]
    db.logs.aggregate(pipee,allowDiskUse=True)
    result = list(result)
    print(result)
#    for element in result:
        #pprint.pprint(element)
#        db.aplicacion.insert_one(element)
    print("Listo")

def lectorVirus(fechai,fechaf): #Lector Virus
    print("MMMMMMMMMM")
    pipee = [
        {"$sort":{"date":1}},
        {"$match": {"$and": [{"date": {"$gte": fechai, "$lte": fechaf}},{"subtype":'virus'}]}},
        {"$group": {"_id":{"Fecha":"$date","Empresa":"$devname","hora":"$time","ip":"$srcip","usuario":"$user",'Virus':'$virus',"Accion":"$action"},"count": {"$sum":1}}},
        {"$out":"virus"},
    ]
    db.logs.aggregate(pipee,allowDiskUse=True)

#    for element in result:
        #pprint.pprint(element)
#        db.aplicacion.insert_one(element)
    print("Listo")


def prueba(fechai,fechaf,empresa): #Top 10 paginas
    graph = pygal.Bar()
    pipee = [

        {"$match": {"$and": [{"_id.Empresa": empresa},{"_id.Fecha": {"$gte": fechai, "$lte": fechaf}}]}},
        {"$group": {"_id": "$_id.categoria",'count':{'$sum':1}}},
        {"$sort": {"count": -1}},
    ]
    result = db.pruebas.aggregate(pipee,allowDiskUse=True)

    result = list(result)
    pprint.pprint(result)

initialDate = "2018-01-01"
finalDate = "2020-07-11"
empresa = 'HA-RNT FG100D'

start =time.time()
lectorWeb(initialDate, finalDate)
lectorApp(initialDate, finalDate)
lectorVirus(initialDate, finalDate)
lectorAppWifi(initialDate, finalDate)

print(time.time()-start)
