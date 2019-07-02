from flask import Flask, render_template,request,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from content_management import content,datosEmpresa,Tablas
from funciones import *


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'RealNet2019'
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
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
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
        graph_6 = tb6_prod(initialDate, finalDate,empresa)

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
        grafica6=graph_6,
        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph = graph_1(fechai, fechaf,empresa)
        graph_2 = tb1_prod(fechai,fechaf,empresa)
        graph_3 = tb3_prod(fechai,fechaf,empresa)
        graph_4 = tb4_prod(fechai,fechaf,empresa)
        graph_5 = tb5_prod(fechai,fechaf,empresa)
        graph_6 = tb6_prod(fechai,fechaf,empresa)

        return render_template("/puntos/productividad.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph,
        grafica2=graph_2,
        grafica3=graph_3,
        grafica4=graph_4,
        grafica5=graph_5,
        grafica6=graph_6,
        )

@app.route('/riesgoslegales',methods=["POST","GET"])
def riesgoslegales():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_rl(initialDate, finalDate,empresa)
        graph2 = tb2_rl(initialDate, finalDate,empresa)
        graph3 = tb3_rl(initialDate, finalDate,empresa)
        graph4 = tb4_rl(initialDate, finalDate,empresa)


        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/legales.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph1 = tb1_rl(fechai, fechaf,empresa),
        graph2 = tb2_rl(fechai, fechaf,empresa),
        graph3 = tb3_rl(fechai, fechaf,empresa),
        graph4 = tb4_rl(fechai, fechaf,empresa),

        return render_template("/puntos/legales.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,

        )

@app.route('/fraudes',methods=["POST","GET"])
def fraudes():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_fd(initialDate, finalDate,empresa)
        graph2 = tb2_fd(initialDate, finalDate,empresa)
        graph3 = tb3_fd(initialDate, finalDate,empresa)
        graph4 = tb4_fd(initialDate, finalDate,empresa)
        graph5 = tb5_fd(initialDate, finalDate,empresa)
        graph6 = tb6_fd(initialDate, finalDate,empresa)

        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/fraudes.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        grafica5=graph5,
        grafica6=graph6,
            )
    else:
        fechai = "2018-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"

        graph1 = tb1_fd(fechai,fechaf,empresa)
        graph2 = tb2_fd(fechai,fechaf,empresa)
        graph3 = tb3_fd(fechai,fechaf,empresa)
        graph4 = tb4_fd(fechai,fechaf,empresa)
        graph5 = tb5_fd(fechai,fechaf,empresa)
        graph6 = tb6_fd(fechai,fechaf,empresa)

        return render_template("/puntos/fraudes.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        grafica5=graph5,
        grafica6=graph6,)

@app.route('/robo',methods=["POST","GET"])
def robo():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_rf(initialDate, finalDate,empresa)
        graph2 = tb2_rf(initialDate, finalDate,empresa)
        graph3 = tb3_rf(initialDate, finalDate,empresa)
        graph4 = tb4_rf(initialDate, finalDate,empresa)
        graph5 = tb5_rf(initialDate, finalDate,empresa)
        graph6 = tb6_rf(initialDate, finalDate,empresa)

        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/robo.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        grafica5=graph5,
        grafica6=graph6,
        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph1 = tb1_rf(fechai, fechaf,empresa),
        graph2 = tb2_rf(fechai, fechaf,empresa),
        graph3 = tb3_rf(fechai, fechaf,empresa),
        graph4 = tb4_rf(fechai, fechaf,empresa),
        graph5 = tb5_rf(fechai, fechaf,empresa),
        graph6 = tb6_rf(fechai, fechaf,empresa),


        return render_template("/puntos/robo.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        grafica5=graph5,
        grafica6=graph6,

        )

        return render_template("/puntos/robo.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)

@app.route('/lealtad',methods=["POST","GET"])
def lealtad():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_ld(initialDate, finalDate,empresa)
        graph2 = tb2_ld(initialDate, finalDate,empresa)
        graph3 = tb3_ld(initialDate, finalDate,empresa)

        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/lealtad.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,

        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph1 = tb1_ld(fechai, fechaf,empresa),
        graph2 = tb2_ld(fechai, fechaf,empresa),
        graph3 = tb3_ld(fechai, fechaf,empresa),


        return render_template("/puntos/lealtad.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        )
@app.route('/evasion',methods=["POST","GET"])
def evasion():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_ev(initialDate, finalDate,empresa)
        graph2 = tb2_ev(initialDate, finalDate,empresa)
        graph3 = tb3_ev(initialDate, finalDate,empresa)
        graph4 = tb4_ev(initialDate, finalDate,empresa)
        graph5 = tb5_ev(initialDate, finalDate,empresa)

        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/evasion.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        grafica5=graph5,
        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph1 = tb1_ev(fechai, fechaf,empresa),
        graph2 = tb2_ev(fechai, fechaf,empresa),
        graph3 = tb3_ev(fechai, fechaf,empresa),
        graph4 = tb4_ev(fechai, fechaf,empresa),
        graph4 = tb4_ev(fechai, fechaf,empresa),
        graph5 = tb5_ev(fechai, fechaf,empresa),



        return render_template("/puntos/evasion.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        grafica3=graph3,
        grafica4=graph4,
        grafica5=graph5,

        )
@app.route('/bandwidth',methods=["POST","GET"])
def bandwidth():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_bd(initialDate, finalDate,empresa)
        graph2 = tb2_bd(initialDate, finalDate,empresa)


        if not graph1:
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/bandwidth.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph1 = tb1_bd(fechai, fechaf,empresa),
        graph2 = tb2_bd(fechai, fechaf,empresa),

        return render_template("/puntos/bandwidth.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,
        grafica2=graph2,
        )
@app.route('/politicas',methods=["POST","GET"])
def politicas():
    estado = 1
    if request.method =="POST":
        initialDate = request.form['start']
        finalDate = request.form['end']
        empresa = request.form['empresa']

        graph1 = tb1_ep(initialDate, finalDate,empresa)


        if (graph1==None):
            estado = 0
            flash("La busqueda no arrojo resultados. Intenta con diferente información")
        return render_template("/puntos/politicas.html", Puntos=Puntos,initialDate=initialDate,estado=estado,empresa=empresa,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,

        )
    else:
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph1 = tb1_ep(fechai, fechaf,empresa),


        return render_template("/puntos/politicas.html",Puntos=Puntos,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas,
        grafica1=graph1,

        )
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
        fechai = "2019-01-01"
        fechaf = "2020-01-01"
        empresa = "FG-Rhino-CDMX"
        graph = graph_1(fechai, fechaf,empresa)

        return render_template("/puntos/reportes.html",Puntos=Puntos,grafica1=graph,estado=estado,dEmpresa=dEmpresa,dTablas=dTablas)


if __name__ == "__main__":
    app.run(debug=True)
