import turtle
import time
screen = turtle.Screen()
screen.bgcolor("black")
bunga = turtle.Turtle()
bunga.speed(0)
bunga.width(2)
def gambar_bunga():
    for i in range(36):
        bunga.color("pink")
        bunga.circle(100)
        bunga.left(10)
while True:
    bunga.clear()
    gambar_bunga()
    bunga.right(5)  # bunga berputar
    time.sleep(0.1)

turtle.done()
