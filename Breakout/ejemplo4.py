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

score = 0
vidas = 3

ball = pygame.image.load("Breakout/imagen/Pokeball.png")
ball= pygame.transform.scale(ball,(40,40))
paddle=pygame.image.load("Breakout/imagen/barra.png")
paddle= pygame.transform.scale(paddle,(80,29))

ladrillos = []
ladrillo_eje_x=20
ladrillo_eje_y=50

for i in range(3):
    fila_ladrillos=[]
    for i in range(12):
        fila_ladrillos.append(pygame.Rect(ladrillo_eje_x+i*50,ladrillo_eje_y,45,20))
    ladrillo_eje_y=ladrillo_eje_y+30
    ladrillo_eje_x=20
    ladrillos.append(fila_ladrillos)



    
ballrect = ball.get_rect()
paddlerect=paddle.get_rect()

speed =[randint(3,6), randint(3,6)]
ballrect.move_ip(WIDTH/2,400)
paddlerect.move_ip(WIDTH/2-20,450)


fuente = pygame.font.Font(None,36)

texto=fuente.render("Game Over",True,(125,125,125))
texto_rect=texto.get_rect()
textoX=ventana.get_width()/2-texto_rect.width/2
textoY=ventana.get_height()/2-texto_rect.height/2


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
    if keys[pygame.K_SPACE] and perder==False:
        pausa=False


    #Compruebo si hay colision
    if paddlerect.colliderect(ballrect):
        # if paddlerect.midleft:
        #     speed[0] = - randint(3, 6)
        # if paddlerect.midright:
        #     speed[0] = randint(3, 6)
        speed[1]= - randint(3,6)
        speed[0]= randint(3,6)
    
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

    # Perder vidas
    if ballrect.bottom > ventana.get_height():
        vidas=vidas-1
        if vidas==0:
            perder=True
        else:
            pausa=True
            speed[0]=0
            speed[1]=0
            ballrect = ball.get_rect()
            paddlerect = paddle.get_rect()
            ballrect.move_ip(WIDTH/2, 400)
            paddlerect.move_ip(WIDTH / 2 - 20, 450)
            speed =[randint(3,6), randint(3,6)]
    



    
    ventana.fill((0,0,0))
    ventana.blit(ball,ballrect)
    ventana.blit(paddle, paddlerect)

    if len(ladrillos)<1:
        speed[0]=0
        speed[1]=0
        font = pygame.font.Font(None, 34)
        text = font.render("Has ganado", True, (255,255,255))
        ventana.blit(text, (250,250))

    if perder:
        ventana.blit(texto, [textoX,textoY])
        if keys[pygame.K_KP_ENTER]:
            perder = False
            ballrect = ball.get_rect()
            paddlerect = paddle.get_rect()
            speed = [randint(3, 6), randint(3, 6)]
            ballrect.move_ip(WIDTH/2, 400)
            paddlerect.move_ip(WIDTH / 2 - 20, 450)
            pausa=True
            score=0
            vidas=3
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), True, (255,255,255))
    ventana.blit(text, (20,10))
    text = font.render("Lives: " + str(vidas), 1, (255,255,255))
    ventana.blit(text, (500,10))  
 
    for fila in ladrillos:
        for ladrillo in fila:
            pygame.draw.rect(ventana,ORANGE, ladrillo)
            if ladrillo.colliderect(ballrect):
                speed[1]=-speed[1]
                fila.remove(ladrillo)
                score=score+100
                if len(fila)==0:
                    ladrillos.remove(fila)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()