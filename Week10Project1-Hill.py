from turtle import Turtle
import math

def drawCircle(turtle, x, y, radius):
    """Draws a circle with given center coordinates and radius."""
    distance = 2.0 * math.pi * radius / 120

    # Moving the turtle to the given x,y coordinates for the center
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()

    # Moving turtle given distance 120 times for full circle
    for i in range(0, 120):
        turtle.forward(distance)
        turtle.left(3)
    turtle.hideturtle()
