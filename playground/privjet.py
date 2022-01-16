import turtle
import numpy as np
t=turtle.Turtle()
print(np.sqrt(2))

screen=turtle.Screen()
screen.setup(1500,1000)
screen.bgcolor('red')
t.penup()
t.setpos(0,0)
t.pendown()
t.pensize(20)
 
def makesichel():
    t.pensize(20)
    t.fillcolor('yellow')
    t.pencolor('yellow')
    t.begin_fill()
    t.left(45)
    t.forward(150)
    t.right(90)
    t.circle(200, 180)
    t.right(180)
    t.circle(-180, 180)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.left(45)


def makestar():
    t.pensize(20)
    t.pencolor('yellow')
    for k in range(5):
        t.forward(150)
        t.right(144)

def makehammer():
    t.pensize(20)
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(100)
    t.left(135)
    t.forward(np.square(2)*20)
    t.left(45)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(400)
    t.end_fill()
    t.left(45)

t.penup()
t.setpos(-400,-200)
t.pendown()
makesichel()
t.penup()
t.setpos(75,-200)
t.pendown()
makehammer()
t.penup()
t.setpos(-150,350)
t.pendown()
makestar()
turtle.done()
