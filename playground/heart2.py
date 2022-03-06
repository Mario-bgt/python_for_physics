# Import turtle package
import turtle
from random import randint

# Creating a turtle object(pen)
pen = turtle.Turtle()
screen=turtle.Screen()
screen.setup(1500,1000)
screen.bgcolor('green')

# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        turtle.right(1)
        turtle.forward(1)
# Defining method to draw a full heart
def heart():
    # Set the fill color to red
    turtle.fillcolor('red')

    # Start filling the color
    turtle.begin_fill()

    # Draw the left line
    turtle.left(140)
    turtle.forward(113)

    # Draw the left curve
    curve()
    turtle.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    turtle.forward(112)

    # Ending the filling of the color
    turtle.end_fill()

pen.ht()
# Draw a heart
for k in range(50):
    x = randint(-600, 600)
    y = randint(-400, 400)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    heart()


# To hide turtle
turtle.done()
