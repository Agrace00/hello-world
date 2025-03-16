import turtle

INITIAL_SIZE = 100

def koch_snowflake(t, order, length):

    if order == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, length/3)
            t.left(angle)

myTurtle = turtle.Turtle()

for _ in range(3):
    koch_snowflake(myTurtle, 0, INITIAL_SIZE)
    myTurtle.right(120)

myTurtle.penup()
myTurtle.goto(-75, -100)
myTurtle.pendown()

for _ in range(3):
    koch_snowflake(myTurtle, 1, INITIAL_SIZE)
    myTurtle.right(120)

myTurtle.penup()
myTurtle.goto(-125, -200)
myTurtle.pendown()

for _ in range(3):
    koch_snowflake(myTurtle, 2, INITIAL_SIZE)
    myTurtle.right(120)

turtle.done()
