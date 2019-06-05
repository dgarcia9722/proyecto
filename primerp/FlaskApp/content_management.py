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
        "FWF90D3Z13000359",
        "FWFRNT",
        "Allan",
    ]}
    return nPuntos,nEmpresas
def Tablas():
    Analisis = {
        1:["Top 10 categorias"],
        2: [{"Top"}],

    }
    return Analisis
#Analisis = Tablas()
#print(Analisis['Top 10 categorias'])