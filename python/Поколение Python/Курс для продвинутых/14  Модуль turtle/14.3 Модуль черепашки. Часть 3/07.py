import turtle as t

radius = 200
colors = ['#ffab00' ,'#052dfe']
t.Screen().bgcolor(colors[1])

t1 = t.Turtle()
t1.hideturtle()
t1.pensize(radius)
t1.pencolor(colors[0])
t1.dot()

t2 = t.Turtle()
t2.hideturtle()
t2.pensize(radius)
t2.pencolor(colors[1])
t2.penup()

t.tracer(12, 0.12)
for _ in range(2*radius, -2*radius - 5, -5):
    t2.clear()
    t2.setx(_)
    t2.dot()
    
t.exitonclick()