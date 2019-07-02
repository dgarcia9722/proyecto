from jinja2 import FileSystemLoader, Environment
from funcionesReportes import *
import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pdfkit
from content_management import *
import time

client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros

env = Environment(loader=FileSystemLoader(searchpath="templates"))
template = env.get_template("find.html")


path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
options = {
    'page-size': 'Letter',
    'encoding': "UTF-8",
    'header-html': './templates/salidaReporte/archivos/header.html',
    'footer-html': './templates/salidaReporte/archivos/footer.html',
    'margin-top': '50mm',
    'margin-left': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '40mm'
}



def main():
    client = MongoClient('mongodb://172.16.11.20:27017/')
    db = client.registros
    dempresa = db.empresas.find()
    dempresa = list(dempresa)
    fecha = dempresa[0]['inicio']
    encargado = dempresa[0]['encargado']
    diae = datetime.strptime(fecha,'%Y-%m-%d')
    diah = datetime.now()
    diam = datetime.now()+relativedelta(months=1)
    if diae.day==diah.day:
        print("Son iguales")
    else:
        print("Son diferentes")
    diah = diah.strftime('%Y-%m-%d')
    diam = diam.strftime('%Y-%m-%d')
    Puntos = content()


    initialDate = "2019-01-01"
    finalDate = "2020-01-01"
    empresa = dempresa[0]['devname']
    start =time.time()


    graph_1(initialDate,finalDate,empresa)
    tb1_prod(initialDate,finalDate,empresa)
    tb3_prod(initialDate,finalDate,empresa)
    pd4 = tb4_prod(initialDate,finalDate,empresa)
    pd5 = tb5_prod(initialDate,finalDate,empresa)
    pd6 = tb6_prod(initialDate,finalDate,empresa)
    print(time.time()-start)


    with open("templates/salidaReporte/report.html", "w") as f:
        f.write(template.render(dempresa=dempresa[0],
        iDate=initialDate,
        fDate=finalDate,
        diah=diah,
        diam=diam,
        puntos=Puntos,
        pd4=pd4,
        pd5=pd5,
        pd6=pd6,
        ))

    pdfkit.from_file("templates/salidaReporte/report.html","templates/salidaReporte/reporte.pdf",configuration=config,options=options)

if __name__ == "__main__":
    main()
