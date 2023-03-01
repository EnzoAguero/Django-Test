from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render


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

def plantillaParametros(req):
    nombre = "Enzo"
    lenguajes = ["Python","Ruby","JavasScript","C","Kotlin"]
    #Abrimos el doc que tiene la plantilla
    plantillaExterna = open("C:/MiProyecto/MiProyecto/plantillas/plantillaParametros.html")
    template = Template(plantillaExterna.read())
    #Cargar el doc en una variable de tipo "template"
    plantillaExterna.close()
    #Crear un contexto
    contexto = Context({"nombrePersona" : nombre,"lenguajes" : lenguajes})
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaCargado(req):
    nombre = "Enzo"
    lenguajes = ["Python","Ruby","JavasScript","C","Kotlin","Java"]
    #Especificando la carpeta donde se encuentran las plantillas y la almacenamos en una variable
    plantillaExterna = loader.get_template('plantillaParametros.html')
    #Renderizar el documento
    documento = plantillaExterna.render({"nombrePersona" : nombre,"lenguajes" : lenguajes})
    return HttpResponse(documento)

def plantillaShortcut(req):
    nombre = "Enzo"
    lenguajes = ["Python","Ruby","JavasScript","C","Kotlin","Java","C++"]
    return render(req, 'plantillaParametros.html',{"nombrePersona" : nombre,"lenguajes" : lenguajes})

def plantillaHija1(req):
    return render(req, "hija1.html",{})


def plantillaHija2(req):
    return render(req, "hija2.html",{})    