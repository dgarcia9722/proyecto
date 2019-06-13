from flask import Flask, render_template,request,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from FlaskApp.content_management import content,datosEmpresa,Tablas
from FlaskApp.funciones import *
from wtforms import DateTimeField,StringField

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'flaashhh'
Puntos = content()
dEmpresa = datosEmpresa()
dTablas = Tablas()

@app.route('/',methods=["POST","GET"])
def analisis():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']
        graph = graph_1(initialDate, finalDate,empresa)
        graph_2 = tb1_prod(initialDate, finalDate,empresa)


        if (graph==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/analisis.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph,
        grafica2=graph_2,
        )
    else:
        fechai = "2018-05-23"
        fechaf = "2020-05-29"
        empresa = ""
        graph = graph_1(fechai, fechaf,empresa)
        graph_2 = tb1_prod(fechai,fechaf,empresa)
        return render_template("/puntos/analisis.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph,
        grafica2=graph_2,
        grafica3=graph_3)

@app.route('/productividad',methods=["POST","GET"])
def productividad():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']
        graph = graph_1(initialDate, finalDate,empresa)
        graph_2 = tb1_prod(initialDate, finalDate,empresa)
        graph_3 = tb3_prod(initialDate, finalDate,empresa)
        graph_4 = tb4_prod(initialDate, finalDate,empresa)
        graph_5 = tb5_prod(initialDate, finalDate,empresa)



        if (graph==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información                  ")
        return render_template("/puntos/productividad.html", Puntos=Puntos,
        initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph,
        grafica2=graph_2,
        grafica3=graph_3,
        grafica4=graph_4,
        grafica5=graph_5,
        )
    else:
        fechai = "2019-01-01"
        fechaf = "2019-12-31"
        empresa = "Allan"
        graph = graph_1(fechai, fechaf,empresa)
        graph_2 = tb1_prod(fechai,fechaf,empresa)
        graph_3 = tb3_prod(fechai,fechaf,empresa)
        graph_4 = tb4_prod(fechai,fechaf,empresa)
        graph_5 = tb5_prod(fechai,fechaf,empresa)



        return render_template("/puntos/productividad.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph,
        grafica2=graph_2,
        grafica3=graph_3,
        grafica4=graph_4,
        grafica5=graph_5,
        )

@app.route('/riesgoslegales',methods=["POST","GET"])
def riesgoslegales():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_rl(initialDate, finalDate,empresa)
        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/legales.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1
        )
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph1 = tb1_rl(fechai, fechaf,empresa)

        return render_template("/puntos/legales.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1
        )

@app.route('/fraudes',methods=["POST","GET"])
def fraudes():
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
        return render_template("/puntos/fraudes.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/fraudes.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/robo',methods=["POST","GET"])
def robo():
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
        return render_template("/puntos/robo.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/robo.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/lealtad',methods=["POST","GET"])
def lealtad():
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
        return render_template("/puntos/lealtad.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/lealtad.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/evasion',methods=["POST","GET"])
def evasion():
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
        return render_template("/puntos/evasion.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/evasion.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/bandwidth',methods=["POST","GET"])
def bandwidth():
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
        return render_template("/puntos/bandwidth.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/bandwidth.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/politicas',methods=["POST","GET"])
def politicas():
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
        return render_template("/puntos/politicas.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/politicas.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/reportes',methods=["POST","GET"])
def reportes():
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
        return render_template("/puntos/reportes.html", Puntos=Puntos, grafica1=graph,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas)
    else:
        fechai = "2019-05-23"
        fechaf = "2019-05-29"
        empresa = "FWFRNT"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/reportes.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)


if __name__ == "__main__":
    app.run(debug=True)
