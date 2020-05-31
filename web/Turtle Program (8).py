import turtle

sn=turtle.Turtle()
sn.getscreen().bgcolor('yellow')
sn.speed(-8)

sn.penup()
sn.goto(-200,40)
sn.pendown()

sn.color('blue', 'red')

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill ()   
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()


star(sn, 360)

turtle.done()