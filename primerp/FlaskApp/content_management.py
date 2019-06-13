def content():
    Puntos = [
        {"puntos":[
            "Analisis",
            "Productividad",
            "Riesgos legales",
            "Fraudes",
            "Robo de informacion",
            "Lealtad",
            "Evasion",
            "Ancho de banda",
            "Revision de politicas",
            "Reportes",
        ]
    },
        {"idpuntos": [
            "Analisis",
            "Productividad",
            "Riesgos_legales",
            "Fraudes",
            "Robo_de_informacion",
            "Lealtad",
            "Evasion",
            "Ancho_de_banda",
            "Revision_de_politicas",
            "Reportes",
        ]
        }
    ]
    return Puntos
def datosEmpresa():
    nPuntos = {"npuntos":[
        "Analisis",
        "Productividad",
        "Riesgos_legales",
        "Fraudes",
        "Robo_de_informacion",
        "Lealtad",
        "Evasion",
        "Ancho_de_banda",
        "Revision_de_politicas",
        "Reportes",
        ]
    }
    nEmpresas = {"empresas":[
        "HA-RNT FG100D",
        "TLA_HA_1",
        "FG-Rhino-CDMX",
        ]}
    return nPuntos,nEmpresas
def Tablas():
    Productividad = {
        1:["Top 10 categorias web","pd1"],
        2:["Top 10 apps","pd2"],
        3:["Top 10 sitios web","pd3"],
        4:["Top 10 banda ancha web","pd4"],
        5:["Top 10 banda ancha app","pd5"],
        6:["Top 10 uso de banda ancha por usuario","pd6"],


    }
    RiesgosLegales={
        1:["Sitios potencialmente problematicos","rl1"],
        2:["Sitios con contenido adulto ","rl2"],

    }
    return Productividad,RiesgosLegales
#Analisis = Tablas()
#print(Analisis['Top 10 categorias'])
#Para clientes:
#Por filtro web:
#•	Child abuse
#•	Discrimination
#•	Drug abuse
#•	explicit violence
#•	Extremist Groups
#•	Hacking
#•	Illegal or Unethical
#•	Plagiarism
#•	Proxy Avoidance
#•	Abortion
#•	Dating
#•	Gambling
#•	Marijuana
#•	Nudity and Risque
#•	Sports Hunting and War Games
#•	Tobacco
#•	Weapons(Sales)
#•	Malicious Websites
#•	Phishing
#•	Spam URLs
#•	Job search
#Por aplicación:
#•	Proxy
