lista=["Childabuse","Discrimination","Drugabuse","Violence","Exgroups","Hacking","Illegalorunethical","Plagiarism","Proxyav","Abortion","Dating","Gambling","Marijuana","Nudityrisque","SportsHunting","Weapons","Maliciouswebsites","Phishing","Spamurls","Jobsearch"]
lista2 = ["Child abuse","Discrimination","Drug Abuse","Explicit Violence","Extremist Groups","Hacking","Illegal or Unethical","Plagiarism","Proxy Avoidance","Abortion","Dating","Gambling","Marijuana","Nudity and Risque","Sports Hunting and War Games","Weapons(Sales)","Malicious Websites","Phishing","Spam URLs","Job Search"]

for i in range(len(lista)):
    #funcion= "if (diccionario.get('catdesc')=='{} ':\n    email{}(diccionario,infoempresa)".format(lista2[i],lista[i])
    #print(funcion)
    funcion = '''\
    def email{}(diccionario,infoempresa):
        envioCorreo(html,infoempresa)
    '''.format(lista[i])
    print(funcion)
