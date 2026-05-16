import turtle as t
import colorsyss=t.screen()
t.title("NIIN KM")
t.bgcolor('black')
t.tracer(3)
m = 0.9
t.pensize(0)
def drawing(angle, n):
    t.circle(20+n, 100)
    t.left(angle)
    t.circle(20+n, 100)

    t.goto(50,0)
    