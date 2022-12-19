import turtle as t

t.speed(0)

def draw_circle(radius, fillcolor):
    t.fillcolor(fillcolor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
radius = 200
colors = ['#ff2600', '#ffaa00', '#d4fa00', '#31fa00', '#00fa79', '#00fdff', '#0080ff', '#4434ff', '#d83cff', '#ff32a9']

t.penup()
t.goto(0, -radius)
t.pendown()

for _ in range(10):
    draw_circle(radius*(1 - (_ / 10)), colors[_])
    t.penup()
    t.goto(0, -radius + radius*((_ + 1) / 10))
    t.pendown()
    
t.exitonclick()