from Render import Render, color
from  ModelObj import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
SR3 : Obj
"""

########################### Lista de colores para probar
Fondo = color(0,0,0) #negro
Blanco = color(1,1,1)
CYAN = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

###########################################################
# tamaño de la imagen
prueba = Render(1000,500)
# introduzca el tamaño del viewport
#prueba.glViewport(500, 150, 200 ,400)

# ingrese el color del fondo
#prueba.glClearColor(0,0,0)

# ingrese el color para pintar

#prueba.glClear()

######################Punto ##################################
# si quiere pintar un punto es aqui
#prueba.punto(150,275)
#prueba.glColor(1,0,0)
#prueba.punto(100,200)

# quiere pintar una linea, perfecto! aca es el espacio
#prueba.glLinea(-1,1, 1,-1)
#prueba.glLinea(-1,-1,1,1)
#prueba.glLinea(1,0,-1,-1)
#prueba.glLinea(1,-1,1,1)


#################### Model Obj #############################################

#prueba.generacionObj('./modelos/Charizard.obj', (350,100), (20,20))



################# Lab 1####################

polinizacion = [(165, 380), (185, 360), (180, 330) ,(207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

polinizacion2 = [(321, 335) ,(288, 286), (339, 251) ,(374, 302)]

polinizacion3 = [(377, 249), (411, 197), (436, 249)]

polinizacion4 = [(413, 177), (448, 159), (502, 88), (553, 53),(535, 36),(676, 37), (660, 52),(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230) ,(580, 230),(597, 215), (552, 214), (517, 144), (466, 180)]
polinizacion5 = [(682, 175), (708, 120), (735, 148) ,(739, 170)]

prueba.glColor(1,0,0)
prueba.pintaPol(polinizacion)
prueba.glColor(0,1,0)
prueba.pintaPol(polinizacion2)
prueba.glColor(0,1,1)
prueba.pintaPol(polinizacion3)
prueba.glColor(1,0.07,0.57)
prueba.pintaPol(polinizacion4)
prueba.glColor(1,1,0)
prueba.pintaPol(polinizacion5)



prueba.glFinish('Poligono.bmp')



