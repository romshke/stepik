import turtle as t

t.speed(0)
t.pensize(3)

t.circle(100)
t.circle(170)
t.penup()

t.goto(0, 130)
t.pendown()
t.circle(20)
t.goto(0, 50)
t.penup()

t.goto(-90, 190)
t.pensize(20)
t.dot()
t.goto(90, 190)
t.dot()
t.pensize(3)

t.goto(-155, 280)
t.pendown()
t.circle(60)
t.penup()
t.goto(155, 280)
t.pendown()
t.circle(60)

t.exitonclick()