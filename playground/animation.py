from turtle import *


def bogen():
    repeat
    45:
    forward(3)
    right(2)


def blatt():
    startPath()
    bogen()
    right(90)
    bogen()
    left(150)
    fillPath()


def propeller():
    repeat
    3:
    blatt()
    right(120)


makeTurtle()
hideTurtle()
# enableRepaint(False)

repeat:
propeller()
# repaint()
delay(40)
right(4)
clear("gray")