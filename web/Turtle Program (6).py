from turtle import Turtle, Screen

screen=Screen()
t=Turtle("turtle")
t.speed(-1)

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickright(x, y):
    t.clear()

def main():

    t.ondrag(dragging)
    turtle.onscreenclick(clickright, 3)
    turtle.listen()
    screen.mainloop()

Turtle.exitonclick()

main()