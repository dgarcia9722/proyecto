import pprint
from pymongo import MongoClient
import json
import pygal

diccionario = [
{"Ingles":["Hello","Goodbye"]},
{"Español":["Hola","Adios"]},
]
print(diccionario[0]["Ingles"]["Hello"])
