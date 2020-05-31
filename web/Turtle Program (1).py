import turtle

t1=turtle.Turtle()
t1.pencolor('red')
t1.shapesize(1)
t1.pensize(3)

t1.left(150)
for i in range(3):
    t1.forward(100)
    t1.right(90)

t1.forward(100)
t1.right(110)
for i in range(3):
    t1.forward(100)
    t1.right(90)
t1.forward(100)
t1.right(110)
for i in range(4):
    t1.forward(100)
    t1.right(90)

t1.hideturtle()

turtle.exitonclick()