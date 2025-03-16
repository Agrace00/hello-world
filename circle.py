from turtle import Turtle
import math

t = Turtle()

def drawCircle(t, x, y, r):
    distance = 2.0 * math.pi * r / 120.0
    t.penup()
    t.goto(x, y)
    t.pendown()
    for count in range(120):
        t.forward(distance)
        t.left(3)
    t.hideturtle()
