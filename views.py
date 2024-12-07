import datetime
from django.http import HttpResponse

def saludo(request):#primera vista

    return HttpResponse("Hola mundo")

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
