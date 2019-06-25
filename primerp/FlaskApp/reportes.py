from jinja2 import FileSystemLoader, Environment
from funciones import *
import pprint
from datetime import datetime
import pdfkit

client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros

env = Environment(loader=FileSystemLoader(searchpath="templates"))
template = env.get_template("find.html")
content = "Hello, world!"

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
    if diae.day==diah.day:
        print("Son iguales")

    else:
        print("Son diferentes")
    content = dempresa

    initialDate = "2019-01-01"
    finalDate = "2020-01-01"
    empresa = dempresa[0]['devname']
    graph = graph_1(initialDate, finalDate,empresa)
    graph_2 = tb1_prod(initialDate, finalDate,empresa)
    graph_3 = tb3_prod(initialDate, finalDate,empresa)
    graph_4 = tb4_prod(initialDate, finalDate,empresa)
    graph_5 = tb5_prod(initialDate, finalDate,empresa)
    graph_6 = tb6_prod(initialDate, finalDate,empresa)


    with open("templates/salidaReporte/report.html", "w") as f:
        f.write(template.render(content=content,dempresa=dempresa[0],
        grafica1=graph,
        grafica2=graph_2,
        grafica3=graph_3,
        grafica4=graph_4,
        grafica5=graph_5,
        grafica6=graph_6,))
    pdfkit.from_file("templates/salidaReporte/report.html","templates/salidaReporte/reporte.pdf",configuration=config,options=options)

if __name__ == "__main__":
    main()
