from flask import Flask, render_template,request,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from FlaskApp.content_management import content
from FlaskApp.funciones import graph_1
import json
import pygal
import pprint


app = Flask(__name__)
Bootstrap(app)

client = MongoClient('mongodb://asalinas:RealNet2019@192.168.60.9:27017/admin')
db = client.prueba
Puntos = content()

@app.route('/')
def dashboard():
    graph = graph_1()
    return render_template("dashboard.html",Puntos=Puntos,grafica1=graph)

@app.route('/find',methods=["POST","GET"])
def vista():
    datag = graph_1()

    return render_template("find.html",graph_data=datag)




if __name__ == "__main__":
    app.run(debug=True)
