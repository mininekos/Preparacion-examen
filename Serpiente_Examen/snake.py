import time
import turtle
import random


score_manzana=0
score_tortuga=0
high_score=0
delay=0.1

# Configuramos la ventana
wn= turtle.Screen()
wn.title("Serpiente🐍")
wn.bgcolor("LightSalmon")
wn.setup(width=600,height=600)
wn.tracer(0)

# Cabeza de serpiente

cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
# Para no dejar estela
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"

texto = turtle.Turtle()
texto.speed(0)
texto.shape("square")
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 250)
texto.write(f"Manzana: {score_manzana} Tortuga: {score_tortuga} High Score: {high_score}",
            align="center",font=("candara", 24, "bold"))

# La manzana
manzana= turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.goto(random.randint(-280,280),random.randint(-280,260))

# Tortuga
tortuga= turtle.Turtle()
tortuga.speed(0)
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()
tortuga.goto(random.randint(-280,280),random.randint(-280,260))

# El cuerpo de la serpiente
segmentos=[]

def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"
def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"
def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"
def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "right":
        x=cabeza.xcor()
        cabeza.setx(x+20)
    if cabeza.direction == "left":
        x=cabeza.xcor()
        cabeza.setx(x-20)

wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(derecha,"Right")
wn.onkeypress(izquierda,"Left")
while True:
    wn.update()
    # Generar segmento
    def comer(): 
        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("blue")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

    # Comer manzana
    if cabeza.distance(manzana) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        manzana.goto(x, y)
        score_manzana+=10
        if high_score<score_manzana+score_tortuga:
            high_score=score_manzana+score_tortuga
        texto.clear()
        texto.write(f"Manzana: {score_manzana} Tortuga: {score_tortuga} High Score: {high_score}",
            align="center",font=("candara", 24, "bold"))
        comer()

    if cabeza.distance(tortuga)<20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        tortuga.goto(x, y)
        score_tortuga+=10
        if high_score<score_manzana+score_tortuga:
            high_score=score_manzana+score_tortuga
        texto.clear()
        texto.write(f"Manzana: {score_manzana} Tortuga: {score_tortuga} High Score: {high_score}",
            align="center",font=("candara", 24, "bold"))
        comer()

    totalSeg=len(segmentos)

    for index in range(totalSeg -1,0,-1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    if cabeza.ycor() > 280 or cabeza.ycor() < -280 \
            or cabeza.xcor() > 280 or cabeza.xcor() < -280:
        score_manzana = 0
        score_tortuga = 0
        texto.clear()
        texto.write(f"Manzana: {score_manzana} Tortuga: {score_tortuga} High Score: {high_score}",
            align="center",font=("candara", 24, "bold"))
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        manzana.goto(x, y)
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        tortuga.goto(x, y)
        for segmento in segmentos:
            segmento.goto(1000,1000)
        segmentos.clear()
    mov()
    #colision cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            score_manzana = 0
            score_tortuga = 0
            texto.clear()
            texto.write(f"Manzana: {score_manzana} Tortuga: {score_tortuga} High Score: {high_score}",
                align="center",font=("candara", 24, "bold"))
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            x = random.randint(-280, 280)
            y = random.randint(-280, 260)
            manzana.goto(x, y)
            x = random.randint(-280, 280)
            y = random.randint(-280, 260)
            tortuga.goto(x, y)
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmentos.clear()


    time.sleep(delay)