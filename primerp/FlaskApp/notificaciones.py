from pymongo import MongoClient
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cliente = MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["registros"]

def seleccion(diccionario):
    devname = diccionario.get("devname")
    infoempresa = mydb.empresas.find_one({"devname":devname})
#    infoempresa = list(infoempresa)
#    print(infoempresa)
 #   print(len(infoempresa))

#    if not(infoempresa) == None:
   #     print(infoempresa)
  #      print(type(infoempresa))
     #   if not infoempresa[0]['encargado']:
    #        infoempresa[0]['encargado'] = 'No disponible'
#       print("hola")
    if not 'user' in diccionario:
        diccionario['user']='No disponible '
    if (diccionario.get('catdesc')=='Advertising'):
        emailAdvertising(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Child Abuse '):
        emailChildabuse(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Discrimination '):
        emailDiscrimination(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Drug Abuse '):
        emailDrugabuse(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Explicit Violence '):
        emailViolence(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Extremist Groups '):
        emailExgroups(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Hacking '):
        emailHacking(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Illegal or Unethical '):
        emailIllegalorunethical(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Plagiarism '):
        emailPlagiarism(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Proxy Avoidance '):
        emailProxyav(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Abortion '):
        emailAbortion(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Dating '):
        emailDating(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Gambling '):
        emailGambling(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Marijuana '):
        emailMarijuana(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Nudity and Risque '):
        emailNudityrisque(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Sports Hunting and War Games '):
        emailSportsHunting(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Weapons(Sales) '):
        emailWeapons(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Malicious Websites '):
        emailMaliciouswebsites(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Phishing '):
        emailPhishing(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Spam URLs '):
        emailSpamurls(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Job Search '):
        emailJobsearch(diccionario,infoempresa)
    if (diccionario.get('appcat')=='Proxy'):
        emailProxyapp(diccionario,infoempresa)




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

    """.format(infoempresa['encargado'],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'))

    print(html)
    #envioCorreo(html,infoempresa)

def emailChildabuse(diccionario,infoempresa):
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
          es el monitoreo diario de su equipo, el dia de hoy {}, a las {} se detecto el ingreso a {}, nuestro analisis arrojo que es un sitio con contenido referente a abuso infantil, este sitio ha sido verificado por la asociacion reguladora de internet, este sitio puede meter en problemas legales a la compañia dado que es un sitio ilegal. </p>
        <p>A continuacion se muestra la información más detallada:</p>
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
    #envioCorreo(html,infoempresa)
    print(html)

def emailDiscrimination(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailDrugabuse(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailViolence(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailExgroups(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailHacking(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailIllegalorunethical(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailPlagiarism(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailProxyav(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailAbortion(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailDating(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailGambling(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailMarijuana(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailNudityrisque(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailSportsHunting(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailWeapons(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailMaliciouswebsites(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailPhishing(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailSpamurls(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailJobsearch(diccionario,infoempresa):
    envioCorreo(html,infoempresa)

def emailProxyapp(diccionario,infoempresa):
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
          es el monitoreo diario de su equipo, el dia de hoy {}, a las {} se detecto el uso de la aplicación {}, nuestro analisis arrojo que es una aplicación Proxy. Esta aplicación sirve para evadir la seguridad de la red.</p>
        <p>A continuacion se muestra la información más detallada:</p>
        <table class="table">
          <thead>
            <tr>
              <th>Usuario</th>
              <th>IP</th>
              <th>Aplicación</th>
              <th>Tipo</th>
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
            <td>{}</td>
          </tbody>
        </table>
      <div class="container">
      </div>
      </body>
      </html>

    """.format(infoempresa['encargado'],diccionario.get('date'),diccionario.get('time'),diccionario.get('app'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('app'),diccionario.get('appcat'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'))
#    envioCorreo(html,infoempresa)

    print(html)

def envioCorreo(html,infoempresa):
    #sendto = infoempresa[0]['email']
    sendto = 'asalinas@realnet.com.mx'
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

#diccionarior = {'logver': '56', 'timestamp': '1560549058','tz': 'UTC-5', 'devname': 'PG101E-IMESA', 'devid': 'FG101ETK18004534','vd': 'root', 'date': '2019-06-14', 'time': '16:50:58','logid': '0316013056', 'type': 'utm', 'subtype': 'webfilter','eventtype': 'ftgd blk', 'level': 'warning','eventtime': '1560549058', 'policyid': '4','sessionid': '69872110', 'srcip': '192.168.1.53','srcport': '53914', 'srcintf': 'LAN','srcintfrole': 'lan', 'dstip': '104.254.150.108','dstport': '443', 'dstintf':'wan2', 'dstintfrole': 'wan','proto': '6', 'service': 'PING', 'hostname': 'm.adnxs.com', 'profile': 'default', 'action': 'blocked', 'reqtype': 'direct', 'url': '/', 'sentbyte': 517, 'rcvdbyte': 0, 'direction': 'outgoing', 'msg': 'URL belongs to a denied category in policy', 'method': 'domain', 'cat': '17', 'catdesc': 'Child Abuse ', 'crscore': '30', 'crlevel': 'high '}
#diccionario = {'appcat':'Proxy','app':'Turbo.VPN','logver': '56', 'timestamp': '1560549058','tz': 'UTC-5', 'devname': 'PG101E-IMESA', 'devid': 'FG101ETK18004534','vd': 'root', 'date': '2019-06-14', 'time': '16:50:58','logid': '0316013056', 'type': 'utm', 'subtype': 'webfilter','eventtype': 'ftgd blk', 'level': 'warning','eventtime': '1560549058', 'policyid': '4','sessionid': '69872110', 'srcip': '192.168.1.53','srcport': '53914', 'srcintf': 'LAN','srcintfrole': 'lan', 'dstip': '104.254.150.108','dstport': '443', 'dstintf':'wan2', 'dstintfrole': 'wan','proto': '6', 'service': 'PING', 'hostname': 'm.adnxs.com', 'profile': 'default', 'action': 'blocked', 'reqtype': 'direct', 'url': '/', 'sentbyte': 517, 'rcvdbyte': 0, 'direction': 'outgoing', 'msg': 'URL belongs to a denied category in policy', 'method': 'domain', 'cat': '17', 'crscore': '30', 'crlevel': 'high '}


#seleccion(diccionario)
