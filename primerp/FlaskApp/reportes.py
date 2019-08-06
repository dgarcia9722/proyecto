from jinja2 import FileSystemLoader, Environment
from funcionesReportes import *
import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pdfkit
from content_management import *
import time
from fpruebas import *
client = MongoClient('mongodb://172.16.11.20:27017/')
db = client.registros

env = Environment(loader=FileSystemLoader(searchpath="templates"))
template = env.get_template("treporte.html")

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
    dempresa = db.empresas.find({'empresa':'Cidexsa-Aeropuerto'})
    #dempresa = db.empresas.find({'empresa':'TLA HA 1'})
    #dempresa = db.empresas.find({'empresa':'RealNet'})


    dempresa = list(dempresa)
    pprint.pprint(dempresa)
    fecha = dempresa[0]['inicio']
    encargado = dempresa[0]['contacto'][0][0]
    print(encargado)
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
    #empresa = "RealNet"
    empresa = 'Cidexsa-Aeropuerto FWF30D'
    print(empresa)
    start =time.time()

    crep1 = rep1(initialDate,finalDate,empresa)
    crep2 = rep2(initialDate,finalDate,empresa)
    crep3 = rep3(initialDate,finalDate,empresa)
    crep4 = rep4(initialDate,finalDate,empresa)
    crep5 = rep5(initialDate,finalDate,empresa)
    crep6 = rep6(initialDate,finalDate,empresa)
    crep7 = rep7(initialDate,finalDate,empresa)
    crep8 = rep8(initialDate,finalDate,empresa)
    crep9 = rep9(initialDate,finalDate,empresa)
    crep10 = rep10(initialDate,finalDate,empresa)
    crep11 = rep11(initialDate,finalDate,empresa)
    crep12 = rep12(initialDate,finalDate,empresa)

    print(time.time()-start)


    with open("templates/salidaReporte/report.html",encoding='utf-8',mode="w") as f:
        output = template.render(dempresa=dempresa[0],
        iDate=initialDate,
        fDate=finalDate,
        diah=diah,
        diam=diam,
        puntos=Puntos,
        rep1=crep1,
        rep2=crep2,
        rep3=crep3,
        rep4=crep4,
        rep5=crep5,
        rep6=crep6,
        rep7=crep7,
        rep8=crep8,
        rep9=crep9,
        rep10=crep10,
        rep11=crep11,
        rep12=crep12,
        )
        f.write(output)

    pdfkit.from_file("templates/salidaReporte/report.html","templates/salidaReporte/reporte.pdf",configuration=config,options=options)

if __name__ == "__main__":
    main()
