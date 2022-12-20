import turtle as t

t.hideturtle()
t.speed(10)

def figure(n=4, a=250, color='#ffffff'):
    
    t.fillcolor(color)

    t.begin_fill()

    for _ in range(n):
        t.forward(a)
        t.right(360 / n)

    t.end_fill()

sx, sy = -125, 125

t.penup(), t.goto(sx, sy), t.pendown()
figure()

for raw in range(5):
    rng = 3 if raw % 2 == 0 else 2
    x = 0 if raw % 2 == 0 else 50
    t.penup(), t.setx(sx + x), t.pendown()
    for column in range(rng):
        figure(a=50, color='#000000')
        t.penup(), t.setx(sx + x + 100 * (column + 1)), t.pendown()
    t.penup(), t.sety(sy -50 * (raw + 1)), t.pendown()
    
t.exitonclick()