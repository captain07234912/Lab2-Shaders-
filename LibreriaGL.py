import struct

# struct library es para estructuras binarias de datos

"""Universidad del Valle de Guatemala
    Graficas por computadora
    Clase que tiene funciones para todo el curso
    Jorge Suchite Carnet 15293
    07/07/2020

    sdd
"""


# Creador del BMP
# Creador del punto


# 1 byte  reservado en memoria
def char(c):
    return struct.pack('=c', c.encode('ascii'))


# 2  reservado bytes en memoria

def word(w):
    return struct.pack('=h', w)


# 4  reservado bytes en memoria

def dword(d):
    return struct.pack('=l', d)


# colores que son aceptados en bytes pero ahora seran con coordenadas ingresadas de 0 a 1


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


def xcruz(pointA, pointB):
    return (pointA[0]*pointB[1]) - (pointA[1]*pointB[0])

########################### Lista de colores para probar
Fondo = color(0,0,0)
Blanco = color(1,1,1)
CYANS = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)
