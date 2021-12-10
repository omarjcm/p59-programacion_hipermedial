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
    lista = []
    numeros = response.GET['numeros'].split(',')
    for numero in numeros:
        lista.append( int(numero) )
    numeros_ordenados = sorted( lista )
    
    datos = {
        'numeros':numeros_ordenados,
        'estado':'ok',
        'mensaje':'Numeros enteros ordenados exitosamente.'
    }
    return HttpResponse( json.dumps( datos ), content_type='application/json' )