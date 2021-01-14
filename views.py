from django.http import HttpResponse
import datetime
from django.template import Template, Context
import os

#path = os.getcwd()
path= '/home/davidpuerta/hola/mysite/mysite/plantillas/index.html'
print(path) 
def saludo(request):
  doc_saludo=open(path)
  plt = Template(doc_saludo.read())
  doc_saludo.close()
  ctx = Context({})
  documento = plt.render(ctx)
  return HttpResponse(documento)


def queonda(request):
    return HttpResponse("Que onda ")


def date_client(request):
    fecha_actual = datetime.datetime.now()

    documento = """ 
    <html>
    <body>
    <h1>  Fecha y hora : %s</h1>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, year):

    edadActual = 18
    periodo = year-2021
    edadFutura = edadActual + periodo
    documento = """
       <html> <body> <h2>En el año %s tendras %s </h2></body></html>
        """ % (year, edadFutura)
    return HttpResponse(documento)
