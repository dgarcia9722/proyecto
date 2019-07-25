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
    'margin-top': '35mm',
    'margin-left': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '40mm'
}



def main():
    client = MongoClient('mongodb://172.16.11.20:27017/')
    db = client.registros
    dempresa = db.empresas.find()
    dempresa = list(dempresa)
    pprint.pprint(dempresa[1])
    fecha = dempresa[1]['inicio']
    encargado = dempresa[1]['encargado']
    diae = datetime.strptime(fecha,'%Y-%m-%d')
    diah = datetime.now()
    diam = datetime.now()+relativedelta(months=-1)
    if diae.day==diah.day:
        print("Son iguales")
    else:
        print("Son diferentes")
    diah = diah.strftime('%Y-%m-%d')
    diam = diam.strftime('%Y-%m-%d')
    Puntos = content()


    initialDate = diam
    finalDate = diah
    empresa = 'TLA HA 1'
    print(empresa)
    start =time.time()


    an1 = tb1_an(initialDate,finalDate,empresa)
    an2 = tb2_an(initialDate,finalDate,empresa)
    an3 = tb3_an(initialDate,finalDate,empresa)
    an4 = tb4_an(initialDate,finalDate,empresa)
    pd1 = tb1_prod(initialDate,finalDate,empresa)
    pd2 = tb2_prod(initialDate,finalDate,empresa)
    pd3 = tb3_prod(initialDate,finalDate,empresa)
    pd4 = tb4_prod(initialDate,finalDate,empresa)
    print("DSADSA")
    pd4 = list(pd4)
    print(pd4)
    pd1u = tb1u_prod(initialDate,finalDate,empresa)
    pd2u = tb2u_prod(initialDate,finalDate,empresa)
    pd3u = tb3u_prod(initialDate,finalDate,empresa)
    pd4u = tb4u_prod(initialDate,finalDate,empresa)
    rl1 = tb1_rl(initialDate,finalDate,empresa)
    rl2 = tb2_rl(initialDate,finalDate,empresa)
    rl3 = tb3_rl(initialDate,finalDate,empresa)
    rl4 = tb4_rl(initialDate,finalDate,empresa)

    print(time.time()-start)


    with open("templates/salidaReporte/report.html", "w") as f:
        output = template.render(dempresa=dempresa[2],
        iDate=initialDate,
        fDate=finalDate,
        diah=diah,
        diam=diam,
        puntos=Puntos,
        an1=an1,
        an2=an2,
        an3=an3,
        an4=an4,
        pd1=pd1,
        pd2=pd2,
        pd3=pd3,
        pd4=pd4,
        pd1u=pd1u,
        pd2u=pd2u,
        pd3u=pd3u,
        pd4u=pd4u,
        rl1=rl1,
        rl2=rl2,
        rl3=rl3,
        rl4=rl4,

        )
        f.write(output)

    pdfkit.from_file("templates/salidaReporte/report.html","templates/salidaReporte/reporte.pdf",configuration=config,options=options)

if __name__ == "__main__":
    main()
