
import turtle


t = turtle.Turtle()

input()

t.speed(05)
t.goto(-50, -100)

t.penup()
t.fillcolor("yellow")
t.pencolor("black")
t.pensize(3)
t.begin_fill()
t.goto(-100, 100)
t.pendown()
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.goto(-100, 100)
t.end_fill()


t.penup()
t.goto(0, 30)
t.pensize(1)
t.pendown()
t.fillcolor("white")
t.setheading(90)
t.begin_fill()
t.circle(25)
t.circle(-25)
t.end_fill()

t.penup()
t.goto(-15, 30)
t.dot(20)
t.goto(15, 30)
t.dot(20)

t.goto(35, -20)
t.pencolor("orange")
t.pensize(8)
t.pendown()
t.setheading(-90)
t.circle(-35, 180)
t.hideturtle()
