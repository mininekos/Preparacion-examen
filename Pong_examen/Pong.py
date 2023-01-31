import pygame
from random import *


pygame.init()

# Colores ladrillos
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Breakout")

vidas1 = 3
vidas2 = 3

ball = pygame.image.load("Pong_examen/imagen/Pokeball.png")
ball= pygame.transform.scale(ball,(40,40))
paddle=pygame.image.load("Pong_examen/imagen/barra.png")
paddle= pygame.transform.scale(paddle,(80,29))
paddle2=pygame.image.load("Pong_examen/imagen/barra.png")
paddle2= pygame.transform.scale(paddle,(80,29))

ladrillos = []
ladrillo_eje_x=10
ladrillo_eje_y=150

for i in range(2):
    fila_ladrillos=[]
    for i in range(3):
        fila_ladrillos.append(pygame.Rect(ladrillo_eje_x+i*250,ladrillo_eje_y,45,20))
    ladrillo_eje_y=ladrillo_eje_y+150
    ladrillo_eje_x=90
    ladrillos.append(fila_ladrillos)



    
ballrect = ball.get_rect()
paddlerect=paddle.get_rect()
paddlerect2=paddle2.get_rect()

speed =[randint(3,6), randint(3,6)]
ballrect.move_ip(WIDTH/2,400)
paddlerect.move_ip(WIDTH/2-20,450)
paddlerect2.move_ip(WIDTH/2-20,50)


fuente = pygame.font.Font(None,36)

texto=fuente.render("Pulsa espacio para empezar",True,(125,125,125))
texto_rect=texto.get_rect()
textoX=ventana.get_width()/2-texto_rect.width/2
textoY=ventana.get_height()/2-texto_rect.height/2

texto2=fuente.render("Pulsa intro numerico para reiniciar",True,(125,125,125))
texto2_rect=texto2.get_rect()
texto2X=ventana.get_width()/2-texto2_rect.width/2
texto2Y=ventana.get_height()/2-texto2_rect.height/2+texto_rect.height


perder=False
pausa=True

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddlerect.left > 0 and not perder and not pausa:
        paddlerect=paddlerect.move(-5,0)
    if keys[pygame.K_RIGHT] and paddlerect.right < ventana.get_width() and not perder and not pausa :
        paddlerect = paddlerect.move(5, 0)
    if keys[pygame.K_a] and paddlerect2.left > 0 and not perder and not pausa:
        paddlerect2=paddlerect2.move(-5,0)
    if keys[pygame.K_d] and paddlerect2.right < ventana.get_width() and not perder and not pausa :
        paddlerect2 = paddlerect2.move(5, 0)
    if keys[pygame.K_SPACE] and perder==False:
        pausa=False


    #Compruebo si hay colision
    if paddlerect.colliderect(ballrect):
        speed[1]= - randint(3,6)
        # speed[0]= randint(3,6)

    if paddlerect2.colliderect(ballrect):
        speed[1]= randint(3,6)
        # speed[0]= randint(3,6)

    if pausa:
        ballrect=ballrect.move([0,0])
    else:
        ballrect=ballrect.move(speed)
    # Rebote izq/derecha
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    # Rebote arriba 
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Perder vidas jugador 1
    if ballrect.bottom > ventana.get_height():
        vidas1=vidas1-1
        if vidas1==0:
            perder=True
        else:
            pausa=True
            speed[0]=0
            speed[1]=0
            ballrect = ball.get_rect()
            paddlerect = paddle.get_rect()
            paddlerect2 = paddle2.get_rect()
            ballrect.move_ip(WIDTH/2, 400)
            paddlerect.move_ip(WIDTH / 2 - 20, 450)
            paddlerect2.move_ip(WIDTH/2-20,50)
            speed =[randint(3,6), randint(3,6)]

    # Perder vidas jugador 2
    if ballrect.top < 20 :
        vidas2=vidas2-1
        if vidas2==0:
            perder=True
        else:
            pausa=True
            speed[0]=0
            speed[1]=0
            ballrect = ball.get_rect()
            paddlerect = paddle.get_rect()
            paddlerect2 = paddle2.get_rect()
            ballrect.move_ip(WIDTH/2, 50+ballrect.width)
            paddlerect.move_ip(WIDTH / 2 - 20, 450)
            paddlerect2.move_ip(WIDTH/2-20,50)
            speed =[randint(3,6), randint(3,6)]



    
    ventana.fill((0,0,0))
    ventana.blit(ball,ballrect)
    ventana.blit(paddle, paddlerect)
    ventana.blit(paddle2, paddlerect2)

    if perder:
        if vidas1<=0:
            texto=fuente.render("Jugador 2 Win",True,(125,125,125))
        if vidas2<=0:
            texto=fuente.render("Jugador 1 Win",True,(125,125,125))   
        ventana.blit(texto, [textoX,textoY])
        ventana.blit(texto2, [texto2X,texto2Y])
        if keys[pygame.K_KP_ENTER]:
            perder = False
            ballrect = ball.get_rect()
            paddlerect = paddle.get_rect()
            paddlerect2 = paddle2.get_rect()
            speed = [randint(3, 6), randint(3, 6)]
            ballrect.move_ip(WIDTH/2, 400)
            paddlerect.move_ip(WIDTH / 2 - 20, 450)
            paddlerect2.move_ip(WIDTH/2-20,50)
            pausa=True
            vidas1=3
            vidas2=3
    if pausa:
        ventana.blit(texto, [textoX,textoY])
    font = pygame.font.Font(None, 34)
    text = font.render("Vidas 1: " + str(vidas1), True, (255,255,255))
    ventana.blit(text, (20,10))
    text = font.render("Vidas 2: " + str(vidas2), 1, (255,255,255))
    ventana.blit(text, (500,10))  
 
    for fila in ladrillos:
        for ladrillo in fila:
            pygame.draw.rect(ventana,ORANGE, ladrillo)
            if ladrillo.colliderect(ballrect):
                speed[1]=-speed[1]

                

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()