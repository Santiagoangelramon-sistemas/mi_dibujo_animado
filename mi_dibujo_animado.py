import pygame
import sys
import random
import math


rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)
gris = (128, 128, 128)


color_aleatorio = random.randint (0, 255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Dibujo_pygame")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

###########################
# Bucle principal del juego
###########################
while 1:
    clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click sobre boton de cerrar de la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()
    



    # Rellenar la ventana de color 
    ventana.fill(blanco)

                #dibujar linea 
    for _ in range(4000):
   
        linea = random.randint(50, 50 + 350)
        lineas = random.randint(10, 30 + 300)
        lineac = random.randint(50, 50 + 350)
        lineav = random.randint(100, 100 + 350)
        color_linea = random.choice([naranja])
        pygame.draw.line(ventana, color_linea, (linea, lineas), (lineac, lineav))

    #dibujar linea 
    for _ in range(700):
   
        linea = random.randint(50, 50 + 350)
        lineas = random.randint(10, 30 + 300)
        lineac = random.randint(50, 50 + 350)
        lineav = random.randint(100, 100 + 350)
        color_linea = random.choice([amarillo])
        pygame.draw.line(ventana, color_linea, (linea, lineas), (lineac, lineav))

    # rectangulo relleno, ubicado en la coordenada esquina superior izq (200,200),  de ancho 200 y altura 100
    pygame.draw.rect(ventana, rosado, (50,300, 390,150)) # cuerpo_tren1
    pygame.draw.rect(ventana, azul, (50,180, 210,120)) # ventana
    pygame.draw.rect(ventana, rosado, (37,130, 250,50)) # cuerpo_tren2
    pygame.draw.rect(ventana, amarillo, (360,310, 80,70)) # Luz A
    pygame.draw.rect(ventana, gris, (30,130, 260,20)) #superior A
    pygame.draw.rect(ventana, gris, (30,430, 432,20)) #carril A
    pygame.draw.circle(ventana, negro, (80, 450), 53) #llanta1
    pygame.draw.circle(ventana, negro, (360, 450), 53) #llanta3
    pygame.draw.circle(ventana, negro, (220, 450), 53) #llanta2
    pygame.draw.circle(ventana, blanco, (220, 450), 25) #llanta2 (cubierta)
    pygame.draw.circle(ventana, blanco, (360, 450), 25) #llanta3 (cubierta)
    pygame.draw.circle(ventana, blanco, (80, 450), 25) #llanta1 (cubierta)
    pygame.draw.circle(ventana, blanco, (160, 240), 53) #carita yupiliano
    pygame.draw.circle(ventana, negro, (140, 240), 10) #jojos1
    pygame.draw.circle(ventana, negro, (200, 240), 10) #jojos2
    pygame.draw.rect(ventana, negro, (160,260, 25,10)) #carril A
    # Agregar texto
    # Fuente tipo Arial, tamaño 35, negrilla y cursiva.
    fuente_arial = pygame.font.SysFont("Arial", 23, 1, 1)
    texto = fuente_arial.render("Mi primer dibujo en Pygame", 1, negro)
    ventana.blit(texto,(30,20))

    fuente_arial = pygame.font.SysFont("Arial", 23, 1, 1)
    texto = fuente_arial.render("By: Mistery Dream", 1, negro)
    ventana.blit(texto,(35,47))
    # Actualiza la visualizacion de la ventana
    pygame.display.flip()
####################################
# Fin del bucle principal del juego
####################################