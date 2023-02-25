from django.http import HttpResponse
import datetime
from django.template import Template,Context

#Esto es una vista
def bienvenida(req): #Se pasa un objeto req como argumento
    return HttpResponse('Bienvenido :D')

def categoriaEdad (req,edad):
    if(edad >= 18):
        if(edad >= 60):
            categoria = 'Tercera edad'
        else:
            categoria = "Adulto"
    else:
        if(edad < 10):
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"
    resultado = "<h1> Categoria de la edad %s</h1>" %categoria
    return HttpResponse(resultado)

def momentoActual(req):
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    return HttpResponse(respuesta)

def contenidoHtml(req,nombre,edad):
    contenido = """ 
    <html> 
    <body>
    <p>Nombre: %s / Edad %s </p>
    </body>
    </html>
    """ % (nombre,edad)
    return HttpResponse(contenido)

def plantilla(req):
    #Abrimos el doc que tiene la plantilla
    plantillaExterna = open("C:/MiProyecto/MiProyecto/plantillas/plantilla1.html")
    template = Template(plantillaExterna.read())
    #Cargar el doc en una variable de tipo "template"
    plantillaExterna.close()
    #Crear un contexto
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)