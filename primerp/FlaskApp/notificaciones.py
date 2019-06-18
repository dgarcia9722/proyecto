from pymongo import MongoClient
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cliente = MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["registros"]

def seleccion(diccionario,infoempresa):
    if not 'user' in diccionario:
        diccionario['user']='No disponible '
    if (diccionario.get('catdesc')=='Advertising'):
        emailAdvertising(diccionario,infoempresa)



def emailAdvertising(diccionario,infoempresa):
    html = """\
<!DOCTYPE html>
      <html lang="en">
      <head>
        <title>Bootstrap Example</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
      </head>
      <body>
        <p>Hola {}</p>
        <p>Uno de los beneficios de nuestro servicio administrado Productivity Gurú
          es el monitoreo diario de su equipo, el dia de hoy {}, a las {} se detecto el ingreso a {}, nuestro analisis arrojo que es un sitio de publicidad
        a continuacion se muestra la información más detallada:</p>
        <table class="table">
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
            <th scope="row">{}</th>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
          </tbody>
        </table>
      <div class="container">
      </div>
      </body>
      </html>

    """.format(infoempresa[0]['encargado'],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'))
    
    print(html)
    envioCorreo(html,infoempresa)


def envioCorreo(html,infoempresa):
    sendto = infoempresa[0]['email']
    user = 'allan.salinas.ramirez@gmail.com'
    password = 'Reflektor94'
    msg = MIMEMultipart('Alternative')
    msg['Subject'] = "Notificacion prueba"
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

diccionario = {'logver': '56', 'timestamp': '1560549058',
 'tz': 'UTC-5', 'devname': 'PG101E-IMESA', 'devid': 'FG101ETK18004534',
  'vd': 'root', 'date': '2019-06-14', 'time': '16:50:58',
   'logid': '0316013056', 'type': 'utm', 'subtype': 'webfilter',
   'eventtype': 'ftgd blk', 'level': 'warning',
   'eventtime': '1560549058', 'policyid': '4',
   'sessionid': '69872110', 'srcip': '192.168.1.53',
    'srcport': '53914', 'srcintf': 'LAN',
     'srcintfrole': 'lan', 'dstip': '104.254.150.108',
      'dstport': '443', 'dstintf': 'wan2', 'dstintfrole': 'wan',
       'proto': '6', 'service': 'PING', 'hostname': 'm.adnxs.com', 'profile': 'default', 'action': 'blocked', 'reqtype': 'direct', 'url': '/', 'sentbyte': 517, 'rcvdbyte': 0, 'direction': 'outgoing', 'msg': 'URL belongs to a denied category in policy', 'method': 'domain', 'cat': '17', 'catdesc': 'Advertising', 'crscore': '30', 'crlevel': 'high '}
devname = diccionario.get("devname")
infoempresa = mydb.empresas.find({"devname":devname})
infoempresa = list(infoempresa)

seleccion(diccionario,infoempresa)
