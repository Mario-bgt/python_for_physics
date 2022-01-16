import turtle
from random import randint

t = turtle.Turtle()
turtle.shape("turtle")
turtle.colormode(255)
screen = turtle.Screen()
screen.setup(1500, 1000)
screen.bgcolor('red')


def makepenis(size, r, g, b):
    t.color(r, g, b)
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.begin_fill()
    t.circle(size, 360)
    t.circle(-size, 360)
    t.end_fill()
    t.begin_fill()
    t.right(90)
    t.forward(size / 2)
    t.left(90)
    t.forward(size * 4)
    t.circle(size / 2, 180)
    t.forward(size * 4)
    t.end_fill()


for k in range(50):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    k += 1
    makepenis(k * 5, r, g, b)
    t.right(90)
