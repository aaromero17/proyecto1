import datetime
from django.http import HttpResponse
#from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
 


class Persona(object):
    
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request):#primera vista
    persona=Persona("Alex","Romero")
    
    ahora=datetime.datetime.now()
    plantillas=["Plantillas","Bases de datos","Modelos"]
    #doc_externo=open("D:/practicas/django/proyecto1/proyecto1/plantillas/miplantilla.html")
    
    # cargar en settings.py      DIRS': ["D:/practicas/django/proyecto1/proyecto1/plantillas/"]
    
    #plt=Template(doc_externo.read())    
    #doc_externo.close()

    doc_externo=get_template(("miplantilla.html"))

    #ctx=Context({"nombre_persona":persona.nombre,"apellido_persona":persona.apellido,"ahora":ahora,"temas":plantillas})
    #documento=plt.render(ctx)

    diccionario={"nombre_persona":persona.nombre,"apellido_persona":persona.apellido,"ahora":ahora,"temas":plantillas}
    #documento=doc_externo.render(diccionario)

    #return HttpResponse(documento)
    return render(request,"miplantilla.html",diccionario)

def cursoC(request):
    
    ahora=datetime.datetime.now()
    diccionario={"ahora":ahora}

    return render(request,"cursoC.html",diccionario)

    



def damefecha(request):
    fechaactual=datetime.datetime.now()

    documento=f"""
        <html>
        <body>
        <h1>
        fecha y hora actuales: {fechaactual}
        </h1>
        </body>
        
        </html>
        
        """


    return HttpResponse(documento)

def calculaedad(request,edad,year):
    
    edadpara=year-2024
    edad=edad+edadpara
    documento=f"La edad para el año {year} sera de {edad}"

    return HttpResponse(documento)
