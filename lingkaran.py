import turtle

layar = turtle.Screen()
layar.bgcolor("lightblue")

bola = turtle.Turtle()
bola.shape("circle")
bola.color("red")
bola.penup()

for i in range(50):
    bola.forward(5)

turtle.done()
