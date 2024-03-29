from pymongo import MongoClient
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cliente = MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["registros"]

head = """\
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <link href="https://fonts.googleapis.com/css?family=Muli&display=swap" rel="stylesheet">
    <meta content="text/html"charset="utf-8">
    <style>
table {
}
td {
  background-color: #FFFFFF;
  text-align: center;
  padding-top: 5px;
  padding-right: 5px;
  padding-bottom: 5px;
  padding-left: 5px;
}
th {
  background-color: #EE680A;
  color: white;
  text-align: center;
  padding-top: 1px;
  padding-right: 1px;
  padding-bottom: 1px;
  padding-left: 1px;
}
body {
background-color: #FFFFFF;
background-color: #FFFFFF;
font-family: 'Muli', sans-serif;
}
li {
  font-size:18px; text-align:justify;
}
#data{
  font-size:18px; text-align:justify;
}
</style>
    <style type="text/css">
</style>
    <title>Notificaciones AISEC</title>
  </head>
  """
virusp = {
    "tr":"""<p>El tipo de virus que se detecto es del tipo troyano, un virus troyano es un tipo de malware que a menudo se disfraza de software legitimo, el atacante puede realizar actividades sin el consentimiento del usuario<p>""",
    "bdr":""" <p>El tipo de virus que se detecto es del tipo backdoor, esto quiere decir que permite el acceso al sistema de forma remota permitiendole al atacante realizar lo que quiera.""",
    "tr.ransom": "<p>El tipo de virus que se detecto es del tipo ransonware, este tipo de virus impide al usuario a acceder a su sistema, usualmente bloquea la pantalla o encripta la información del usuario, para liberar la información el atacante pide un pago, usualmente en alguna criptomoneda." ,
    "tr.spy":"<p>El tipo de virus que se detecto es un troyano espia, este tiene la capacidad de robar información del usuario sin su consentimiento y mandarla al atacante. ",
    "tr.pwd":"<p>El tipo de virus que se detecto es un troyano que se dedica a robar contraseñas, este busca contraseñas guardadas en el sistema y las manda al atacante.",
    "tr.dldr":"<p>El tipo de virus es un troyano, este se enfoca en descargar archivos maliciosos o en actualizarse.",
    "default":'<p>El tipo de virus que se detecto es un software malicioso que que busca comprometer la seguridad de nuestro equipo<p>'
}

virusc = {
    "exploit":'<p>El tipo de virus que se detecto es un software malicioso que toma ventaja de alguna vulnerabilidad de nuestro sistema, el atacante puede habilitar el acceso remoto a nuestro equipo y asi hacer lo que sea.<p>',
    "default":'<p>El tipo de virus que se detecto es un software malicioso que que busca comprometer la seguridad de nuestro equipo<p>'
}

def seleccion(diccionario):
    devname = diccionario.get("devname")
    infoempresa = mydb.empresas.find_one({"devname":devname})
    if diccionario.get("sentbyte")==None:
        diccionario['sentbyte'] = 0
    if diccionario.get("rcvdbyte")==None:
        diccionario['rcvdbyte'] = 0
    if diccionario.get("hostname")==None:
        diccionario['hostname'] = 'Desconocido'
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
        if(diccionario.get('action')=='blocked'):
            emailHacking(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Illegal or Unethical '):
        emailIllegalorunethical(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Plagiarism '):
        if(diccionario.get('action')=='blocked'):
            emailPlagiarism(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Proxy Avoidance '):
        emailProxyav(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Abortion '):
        if(diccionario.get('action')=='blocked'):
            emailAbortion(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Dating '):
        if(diccionario.get('action')=='blocked'):
            emailDating(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Gambling '):
        if(diccionario.get('action')=='blocked'):
            emailGambling(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Marijuana '):
        if(diccionario.get('action')=='blocked'):
            emailMarijuana(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Nudity and Risque '):
        emailNudityrisque(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Sports Hunting and War Games '):
        if(diccionario.get('action')=='blocked'):
            emailSportsHunting(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Weapons(Sales) '):
        emailWeapons(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Malicious Websites '):
        emailMaliciouswebsites(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Phishing '):
        emailPhishing(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Spam URLs '):
        if(diccionario.get('action')=='blocked'):
            emailSpamurls(diccionario,infoempresa)
    if (diccionario.get('catdesc')=='Job Search '):
        if(diccionario.get('action')=='blocked'):
            emailJobsearch(diccionario,infoempresa)
    if (diccionario.get('appcat')=='Proxy'):
        emailProxyapp(diccionario,infoempresa)
    if (diccionario.get('subtype')=='virus'):
        if(diccionario.get('service')=='POP3'):
            emailVirusmail(diccionario,infoempresa)
            print(diccionario)
        if(diccionario.get('service')=='HTTP'):
            emailVirushttp(diccionario,infoempresa)
            print(diccionario)



def emailAdvertising(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"
    body = """\
  <body>
    <table border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>

                <td style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 style="text-align:left; style='font-size:20px;">Hola {}</h3>
                  <p style='font-size:18px; text-align:justify; '>Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>, nuestro análisis arrojo que es un sitio de publicidad, a continuación se muestra la información más detallada:</p>
        <br>
        <table  width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" style='font-size:18px'>Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center" style='font-size:18px'>Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center" style='font-size:18px'>Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)

    #print(html)
    html = head+body
	    #envioCorreo(html,infoempresa)

def emailChildabuse(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 style="text-align:left; style='font-size:20px;">Hola {}</h3>
                  <p style='font-size:18px; text-align:justify; '>Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio con contenido referente a abuso infantil, este sitio ha sido verificado por la asociación reguladora de internet, este sitio puede meter en problemas legales a la compañia dado que es un sitio ilegal, a continuación se muestra la información más detallada:</p>
        <br>
        <table  width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" style='font-size:18px'>Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center" style='font-size:18px'>Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center" style='font-size:18px'>Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)

def emailDiscrimination(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"
    body = """\
  <body>
    <table border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 style="text-align:left; style='font-size:20px;">Hola {}</h3>
                  <p style='font-size:18px; text-align:justify; '>Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio con contenido racista, este contenido abarca <b>Promoción de grupos racistas,Denigración de grupos etnicos y Superioridad de cualquier grupo, a continuación se muestra la información más detallada:</p>
        <br>
        <table  width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" style='font-size:18px'>Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center" style='font-size:18px'>Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center" style='font-size:18px'>Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    #envioCorreo(html,infoempresa)

def emailDrugabuse(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio referente a sustancias nocivas.</p>
                  <ul>
               <li>Promoción</li>
               <li>Venta</li>
               <li>Preparación</li>
               <li>Cultivación</li>
               <li>Distribución</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)


def emailViolence(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio de contenido violento.</p>
                  <ul>
               <li>Violencia extrema</li>
               <li>Crueldad</li>
               <li>Actos de abuso</li>
               <li>Mutilación</li>
               <li>Muerte</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailExgroups(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"
    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio relacionado a grupos extremistas.</p>
                  <p>El sitio puede contener alguno de los siguientes temas: </p>
                  <ul>
               <li>Grupos radicales</li>
               <li>Grupos militares</li>
               <li>Movimientos antigobiernos</li>
               <li>Movimientos religiosos</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailHacking(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"
    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio con temas relacionados a Hacking.</p>
                  <p>El sitio puede contener alguno de los siguientes temas: </p>
                  <ul>
               <li>Modificación de programas</li>
               <li>Modificación de equipos</li>
               <li>Modificación de computadoras</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailIllegalorunethical(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio con contenido ilegal o no ético.</p>
                  <p>Este sitio ofrece información, métodos o instrucciones para: </p>
                  <ul>
               <li>Acciones fraudulentas</li>
               <li>Conductas ilegales(no violentas)</li>
               <li>Fraudes</li>
               <li>Evasión de impuestos</li>
               <li>Chantajes</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailPlagiarism(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio que puede contener información o herramientas para realizar algún tipo de plagio, este sitio se dedica a la venta y distribución de:</p>
                  <ul>
               <li>Examenes escolares</li>
               <li>Proyectos</li>
               <li>Diplomas</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailProxyav(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio que provee información o herramientas en como burlar la seguridad del equipo PG Guru mediante el uso de Proxy:</p>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailAbortion(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"
    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio de contenido sensible(aborto):</p>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailDating(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"
    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio relacionado a citas:</p>
                  <p>Esto puede abarcar lo siguiente: </p>
             <ul>
               <li>Desarrollo de relaciones personales</li>
               <li>Desarrollo de relaciones romanticas </li>
               <li>Relaciones de ámbito sexual</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailGambling(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio relacionado a juegos de apuestas:</p>
                  <p>Esto puede abarcar lo siguiente: </p>
             <ul>
               <li>Loterias</li>
               <li>Apuestas</li>
               <li>Casinos</li>
             </ul>
             <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailMarijuana(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio con información acerca de la cultivación, preparación y uso de marihuana, a continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailNudityrisque(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio con contenido adulto(18+), esto puede ser desnudez parcial o total pero sin insinuación sexual. A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailSportsHunting(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio relacionado a:</p>
                  <ul>
               <li>Juegos de caza</li>
               <li>Juegos de guerra </li>
               <li>Paintball </li>
             </ul>
             <p>Ademas de grupos, clubs y organizaciones relacionados a los puntos anteriores.</p>
           <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)


def emailWeapons(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio relacionado a venta de armamento, esto puede ser de forma legal o ilegal, abarcando la venta de pistolas, rifles, etc. A continuación se muestra la información mas detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailMaliciouswebsites(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio malicioso, entre los riesgos que puede representar el acceso a este sitio esta la descarga de software malicioso, que puede acceder a nuestra información.</p>
                  <p>Los posibles riesgos que puede representar este software son: </p>
             <ul>
               <li>Dañar nuestro equipo</li>
               <li>Atacar nuestro equipo ocasionando perdida de información </li>
               <li>Manipular nuestra información </li>
             </ul>
             <p>Todo lo anterior sin el consentimiento del usuario.
           <p>A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailPhishing(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio falso. Esto se realiza mediante la clonación del sitio original y así engañar al usuario para que ingrese sus datos.</p>
                  <p>Los tipos de páginas que son más recurrentes son del tipo: </p>
             <ul>
               <li>Sitios relacionados a bancos o finanzas</li>
               <li>Sitios con información personal del usuario</li>
               <li>Redes sociales</li>
             </ul>
           <p>A continuación se muestra la información más detallada:</p>

        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailSpamurls(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro análisis arrojo que es un sitio relacionado a publicidad, regularmente se encuentran en correos spam.</p>
                  <p>Puede contener publicidad referente a lo siguiente: </p>
             <ul>
               <li>Sitios sexuales</li>
               <li>Sitios fraudulentos</li>
               <li>Material ofensivo</li>
             </ul>
           <p>A continuación se muestra la información más detallada:</p>

        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailJobsearch(diccionario,infoempresa):
    if diccionario.get('action')=='blocked':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Este sitio representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el ingreso a <b>{}</b>,nuestro analisis arrojo que es un sitio relacionado a búsqueda de trabajo.</p>
                  <p>Este sitio puede contener lo siguiente:</p>
             <ul>
               <li>Información acerca de búsqueda de empleo</li>
               <li>Búsqueda de empleo</li>
               <li>Servicios de consultoría</li>
             </ul>
           <p>A continuación se muestra la información más detallada:</p>

        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>HOST</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('hostname'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('hostname'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    #envioCorreo(html,infoempresa)
    print(html)
    envioCorreo(html,infoempresa)

def emailProxyapp(diccionario,infoempresa):
    if diccionario.get('action')=='block':
        accion = "<p>Gracias a nuestro servicio esta página fue bloqueada exitosamente."
    else:
        accion = "<p>Esta aplicacion representa una vulnerabilidad para tu red, por lo que recomendamos contactar al equipo de Productivity Guru para realizar un chequeo de la red"

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se detecto el uso de la aplicación <b>{}</b>,nuestro análisis arrojo que es una aplicación Proxy. Esta aplicación sirve para evadir la seguridad de la red. A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>APLICACIÓN</th>
              <th>TIPO</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

      """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('app'),diccionario.get('user'),diccionario.get('srcip'),diccionario.get('app'),diccionario.get('appcat'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
      html = head+body
#    envioCorreo(html,infoempresa)

    print(html)

def emailVirushttp(diccionario,infoempresa):
    accion = "<p>Gracias a nuestro servicio el virus fue bloqueado exitosamente.</p>"
    virus = diccionario.get('virus')

    tvirus = virus.split('!')
    for element in virusp.keys():
        if element==tvirus[len(tvirus)-1]:
            virusr = virusp.get(element)
            break
            print(virusr)
        else:
            virusr = virusp.get('default')

    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se hizo la detección del virus con nombre:<b>{}</b>, el virus llegó a través del sitio <b>{}</b> .<b>{}</b> A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>VIRUS</th>
              <th>SITIO</th>
              <th>BYTES RECIBIDOS</th>
              <th>BYTES ENVIADOS</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>

    """.format(infoempresa['contacto'][0][0],diccionario.get('date'),diccionario.get('time'),diccionario.get('virus'),diccionario.get('url'),virusr,diccionario.get('user'),diccionario.get('srcip'),diccionario.get('virus'),diccionario.get('url'),diccionario.get('rcvdbyte'),diccionario.get('sentbyte'),accion)
    html = head+body
    envioCorreo(html,infoempresa)

def emailVirusmail(diccionario,infoempresa):
    accion = "<p>Gracias a nuestro servicio el virus fue bloqueado exitosamente.</p>"
    virus = diccionario.get('virus')
    print(virus)
    tvirus = virus.split('!')
    if not 'from' in diccionario:
        diccionario['from']='No disponible '
    if not 'recipient' in diccionario:
        diccionario['recipient']='No disponible '

    for element in virusc.keys():
        if element==tvirus[len(tvirus)-1]:
            virusr = virusc.get(element)
            break
            print(virusr)
        else:
            virusr = virusc.get('default')
    print(virusr)
    body = """\
  <body>
    <table  border="0px " align="center" cellspacing="0px" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
      <tr>
        <td style="border: 0px ; height: 0px; text align: center; padding: 0px;"><img align="right" width="140" height="60" src="http://aisec.com.mx/images/productivitygurulogo.png">
        </td>
      </tr>
        <tr>
          <td>
            <table  border="0px " cellspacing="0" cellpadding="0px" width="600" style="margin-left: auto; margin-right: auto; height:auto; background-color: #ffffff; margin-top: 0px;">
              <tr>
                <td id="data" style="padding: 10px; width:400px; border: 0px ; halign:top;">
                  <h3 >Hola {}</h3>
                  <p >Uno de los beneficios de nuestro  servicio <b>Productivity Gurú</b> es el monitoreo diario de su equipo, el día de hoy <b>{}</b>, a las <b>{}</b> se hizo la detección del virus con nombre:<b>{}</b>, el virus llegó a traves del sitio <b>{}</b> .<b>{}</b> A continuación se muestra la información más detallada:</p>
        <br>
        <table width="600"  >
          <thead>
            <tr>
              <th>USUARIO</th>
              <th>IP</th>
              <th>VIRUS</th>
              <th>SITIO</th>
              <th>EMISOR</th>
              <th>RECEPTOR</th>
            </tr>
          </thead>
          <tbody>
            <td scope="row">{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <tr>
        </td>
        </tr>
    </table>
    </td>
    </tr>
    <tr>
      <td id="data" style="border: 0px ; cellspacing: 0; cellpadding: 10px; width: 100%; height: auto">
        <p align="center" >Gracias a nuestro servicio esta página fue bloqueada exitosamente</p>
        <p align="center">Cualquier duda o comentario estamos a sus ordenes</p>
        <p align="center">Saludos cordiales </p>
        <p align="center"><img  width="570" height="140" src="http://aisec.com.mx/images/firmageneral.jpg"></p>
        <p align=center style='font-size:16px'>Contacto. (55) 5219 8656   Ext. 215 | www.realnet.com.mx</p>
        </td>
        </tr>
    </table>
  </body>
</html>


    """.format(diccionario.get('date'),diccionario.get('time'),diccionario.get('virus'),diccionario.get('url'),virusr,diccionario.get('user'),diccionario.get('srcip'),diccionario.get('virus'),diccionario.get('url'),diccionario.get('from'),diccionario.get('recipient'),accion)
    html = head+body
    envioCorreo(html,infoempresa)



def envioCorreo(html,infoempresa):
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


#diccionarior = {'logver': '56', 'timestamp': '1560549058','tz': 'UTC-5', 'devname': 'PG101E-IMESA', 'devid': 'FG101ETK18004534','vd': 'root', 'date': '2019-06-14', 'time': '16:50:58','logid': '0316013056', 'type': 'utm', 'subtype': 'webfilter','eventtype': 'ftgd blk', 'level': 'warning','eventtime': '1560549058', 'policyid': '4','sessionid': '69872110', 'srcip': '192.168.1.53','srcport': '53914', 'srcintf': 'LAN','srcintfrole': 'lan', 'dstip': '104.254.150.108','dstport': '443', 'dstintf':'wan2', 'dstintfrole': 'wan','proto': '6', 'service': 'PING', 'hostname': 'm.adnxs.com', 'profile': 'default', 'action': 'blocked', 'reqtype': 'direct', 'url': '/', 'sentbyte': 517, 'rcvdbyte': 0, 'direction': 'outgoing', 'msg': 'URL belongs to a denied category in policy', 'method': 'domain', 'cat': '17', 'catdesc': 'Child Abuse ', 'crscore': '30', 'crlevel': 'high '}
#diccionario = {'appcat':'Proxy','app':'Turbo.VPN','logver': '56', 'timestamp': '1560549058','tz': 'UTC-5', 'devname': 'PG101E-IMESA', 'devid': 'FG101ETK18004534','vd': 'root', 'date': '2019-06-14', 'time': '16:50:58','logid': '0316013056', 'type': 'utm', 'subtype': 'webfilter','eventtype': 'ftgd blk', 'level': 'warning','eventtime': '1560549058', 'policyid': '4','sessionid': '69872110', 'srcip': '192.168.1.53','srcport': '53914', 'srcintf': 'LAN','srcintfrole': 'lan', 'dstip': '104.254.150.108','dstport': '443', 'dstintf':'wan2', 'dstintfrole': 'wan','proto': '6', 'service': 'PING', 'hostname': 'm.adnxs.com', 'profile': 'default', 'action': 'blocked', 'reqtype': 'direct', 'url': '/', 'sentbyte': 517, 'rcvdbyte': 0, 'direction': 'outgoing', 'msg': 'URL belongs to a denied category in policy', 'method': 'domain', 'cat': '17', 'crscore': '30', 'crlevel': 'high '}


#seleccion(diccionario)
