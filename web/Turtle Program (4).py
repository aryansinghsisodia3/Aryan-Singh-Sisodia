import turtle

tim=turtle.Turtle()

tim.width(5)

tim.color('orange','yellow')

tim.begin_fill()
for x in range (4):
    tim.forward(100)
    tim.left(90)
tim.end_fill()

tim.hideturtle()

turtle.exitonclick()