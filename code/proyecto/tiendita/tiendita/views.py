from django.http.response import HttpResponse
from datetime import datetime
import json

def hello_world(response):
    return HttpResponse('Hola mundo')

def hola(response):
    fecha_actual = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse( 'El tiempo del servidor es {}'.format(fecha_actual) )

def obtener_numeros(response):
    numeros = response.GET['numeros']
    return HttpResponse( str(numeros) )

def obtener_numeros_ordenados(response):
    numeros = [ int(i) for i in response.GET['numeros'].split(',') ] 
    numeros_ordenados = sorted( numeros )
    
    datos = {
        'numeros':numeros_ordenados,
        'estado':'ok',
        'mensaje':'Numeros enteros ordenados exitosamente.'
    }
    return HttpResponse( json.dumps( datos ), content_type='application/json' )

def persona(response):
    nombre = response.GET['nombre']
    edad = response.GET['edad']
    edad = int( edad )
    if edad < 12:
        mensaje = 'Lo siento {}, no te encuentras autorizado para estar aqui.'.format(nombre)
    else:
        mensaje = '{}, bienvenido.'.format(nombre)
    return HttpResponse( mensaje )

def persona2(response, nombre, edad):
    if edad < 12:
        mensaje = 'Lo siento {}, no te encuentras autorizado para estar aqui.'.format(nombre)
    else:
        mensaje = '{}, bienvenido.'.format(nombre)
    return HttpResponse( mensaje )
