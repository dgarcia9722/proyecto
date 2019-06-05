from flask import Flask, render_template,request,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from FlaskApp.content_management import content,datosEmpresa,Tablas
from FlaskApp.funciones import graph_1
from wtforms import DateTimeField,StringField

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'flaashhh'
Puntos = content()
dEmpresa = datosEmpresa()
dTablas = Tablas()

@app.route('/',methods=["POST","GET"])
def dashboard():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']
        print(initialDate,finalDate,empresa)
        print(len(empresa))
        graph = graph_1(initialDate, finalDate,empresa)
        if (graph==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("dashboard.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("dashboard.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/find')
def vista():
    datag = graph_1
    return render_template("find.html",graph_data=datag)

@app.route('/prueba')
def prueba():

    return render_template("index.html",Puntos=Puntos)


if __name__ == "__main__":
    app.run(debug=True)
