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
        1:["Sitios potencialmente problematicos PRUEBA","rl1"],
        2:["Sitios con contenido adulto ","rl2"],
        3:["Sitios infectados ","rl3"],
        4:["Aplicaciones peligrosas","rl4"],

    }

    Fraudes={
        1:["Sitios potencialmente problematicos","fd1"],
        2:["Sitios con contenido adulto ","fd2"],
        3:["Sitios infectados ","fd3"],
        4:["Intereses personales ","fd4"],
        5:["Intereses financieros ","fd5"],
        6:["Aplicaciones criticas ","fd6"],
    }
    Robo = {
        1:["Sitios potencialmente problematicos","rb1"],
        2:["Consumo de banda ancha ","rb2"],
        3:["Sitios infectados ","rb3"],
        4:["Intereses personales ","rb4"],
        5:["Intereses financieros ","rb5"],
        6:["Aplicaciones criticas ","rb6"],

    }
    Lealtad = {
        1:["Intereses personales ","ld1"],
        2:["Intereses financieros ","ld2"],
        3:["Aplicaciones criticas ","ld3"],
    }
    Evasion = {
        1:["Sitios potencialmente problematicos","ev1"],
        2:["Consumo de banda ancha ","ev2"],
        3:["Sitios infectados ","ev3"],
        4:["Acceso remoto ","ev4"],
        5:["Aplicaciones criticas ","ev5"],
    }
    Ancho_de_banda = {
        1:["Consumo de banda ancha ","ab1"],
        2:["Aplicaciones criticas ","ab2"],
    }

    Revision_de_politicas = {
        1:["Proteccion de datos ","rp1"],
    }


    Analisis = {
        1:["Consumo de banda ancha ","ans1"],
        2:["Aplicaciones criticas ","ans2"],
    }

    return Productividad,RiesgosLegales,Fraudes,Robo,Lealtad,Evasion,Ancho_de_banda,Revision_de_politicas,
