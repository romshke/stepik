import turtle as t

t.speed(0)

def draw_circle(radius, fillcolor):
    t.fillcolor(fillcolor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
radius = 200
colors = ['#ffb400' ,'#021b9d']

t.bgcolor(colors[1])

t.penup()
t.goto(0, -radius)
t.pendown()

for _ in range(2):
    t.pencolor(colors[_])
    draw_circle(radius, colors[_])
    t.penup()
    t.goto(0.3*radius, -radius)
    t.pendown()
    
t.exitonclick()