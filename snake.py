# Importacion de modulos
import turtle
import time
import random

# Definicion de constantes
posponer = 0.1

# Variables de Marcador
score = 0
high_score = 0

# Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego Snake - Escrito por Dario Nuñez")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntaje: 0  High Score: 0",
            align="center", font=("Courier", 24, "normal"))

# Configuracion de la Cabeza
cabeza = turtle.Turtle()
cabeza.shape("square")
cabeza.speed(0)
cabeza.penup()
cabeza.color("white")
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Configuracion de la Comida
comida = turtle.Turtle()
comida.shape("circle")
comida.speed(0)
comida.penup()
comida.color("red")
comida.goto(0, 100)

# Segmentos - Cuerpo de la Serpiente
segmentos = list()


# Funciones


def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Bucle principal
while True:
    wn.update()
    # Colisiones con el borde de la ventana
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        for i in range(0, len(segmentos)):
            segmentos[i].hideturtle()
        segmentos.clear()
        score = 0
        texto.clear()
        texto.write("Puntaje: {}  High Score: {}".format(score, high_score),
                    align="center", font=("Courier", 24, "normal"))

    # Colisiones con el cuerpo de la serpiente
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            for i in range(0, len(segmentos)):
                segmentos[i].hideturtle()
            segmentos.clear()
            score = 0
            texto.clear()
            texto.write("Puntaje: {}  High Score: {}".format(score, high_score),
                        align="center", font=("Courier", 24, "normal"))

    # Colisiones con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.shape("square")
        nuevo_segmento.speed(0)
        nuevo_segmento.penup()
        nuevo_segmento.color("grey")
        segmentos.append(nuevo_segmento)
        # Aumentar el marcador
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Puntaje: {}  High Score: {}".format(score, high_score),
                    align="center", font=("Courier", 24, "normal"))

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for i in range(totalSeg-1, 0, -1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()
    time.sleep(posponer)
