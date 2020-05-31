import turtle

tim=turtle.Turtle()
tim.color('red', 'yellow')

tim.speed(-1)

tim.begin_fill()
for i in range(95):
    tim.forward(200)
    tim.left(155)
tim.end_fill()


turtle.done()