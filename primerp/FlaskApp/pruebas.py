from pymongo import MongoClient
import pygal
import time
import pprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cairosvg
from funcionesReportes import *
import threading
import queue

initialDate = "2019-05-01"
finalDate = "2019-08-11"
empresa = 'TLA HA 1'
html = """\
 <!DOCTYPE html>
  <html lang="en">
  <head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
  </head>
   <body>
        <p>Hola Allan</p>
        <br>
        <p>Uno de los beneficios de nuestro servicio administrado Productivity Gurú
          es el monitoreo diario de su equipo, el dia de hoy 2019-07-25, a las 11:57 se detecto el ingreso a realnet.com.mx, nuestro analisis arrojo que es un sitio de publicidad
        a continuacion se muestra la información más detallada:</p>
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Usuario</th>
              <th>IP</th>
              <th>Host</th>
              <th>Bytes recibidos</th>
              <th>Bytes enviados</th>
            </tr>
          </thead>
          <tbody>
            <th scope="row">Allan</th>
            <td>192.168.0.50</td>
            <td>realnet.com.mx</td>
            <td>200</td>
            <td>100</td>
          </tbody>
        </table>
        <p>Gracias a nuestro servicio esta página fue bloqueada exitosamente." </p>
        <p>Cualquier duda o comentario estamos a sus ordenes</p>
        <p>Saludos cordiales </p>
      <div class="container">
      </div>
      </body>
      </html>
      """
print(html)
def envioCorreo(html):
    #sendto = infoempresa[0]['email']
    sendto = 'asalinas@realnet.com.mx'
    user = 'admin@aisec.com.mx'
    password = 'h8TaRg80yY,U'
    msg = MIMEMultipart('Alternative')
    msg['Subject'] = "Notificacion AISEC Prueba"
    msg['From'] = user
    msg['To'] = sendto
    part1 = MIMEText(html,'html')
    msg.attach(part1)
    mail = smtplib.SMTPa('mail.aisec.com.mx',587)
    mail.ehlo()
    mail.starttls()
    mail.login(user, password)  
    mail.sendmail(user, sendto, msg.as_string())
    mail.quit


def envioCorreos(html):
    #sendto = infoempresa[0]['email']
    sendto = 'asalinas@realnet.com.mx'
    user = 'allan.salinas.ramirez@gmail.com'
    password = 'Reflektor94'
    msg = MIMEMultipart('Alternative')
    msg['Subject'] = "Notificacion AISEC"
    msg['From'] = user
    msg['To'] = sendto
    part1 = MIMEText(html,'html')
    msg.attach(part1)
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(user, password)
    mail.sendmail(user, sendto, msg.as_string())
    mail.quit

start =time.time()
envioCorreos(html)
#print("WEB")
#tb4_prod(initialDate, finalDate,empresa)
#funcion = tb4_an(initialDate, finalDate,empresa)
#funcion = list(funcion)
#pprint.pprint(funcion)

class MyAccumulator:
    def __init__(self):
        self.sum = 0
    def add(self, number):
        self.sum += number
        return self.sum

class log:
    def __init__(self,empresa,app,conteo):
        self.empresa = empresa
        self.app = app
        self.sum += conteo


A = MyAccumulator()
i = 0
globals()['string%s' %i] = "hola"
print(string0)
globals()['string%s' %i] = "ADios de nuevo"
print(globals()['string%s' %i])

def coroutine(func):
    def wrapper(*args, **kw):
        gen = func(*args, **kw)
        gen.send(None)
        return gen
    return wrapper

@coroutine
def accumulator():
    global vglobal 
    vglobal = "Esto es la global"
    val = 0
    while True:
        val += (yield val)



print(time.time()-start)
