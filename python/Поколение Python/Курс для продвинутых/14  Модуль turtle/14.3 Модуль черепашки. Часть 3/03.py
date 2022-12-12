import turtle as t

t.speed(0)
t.hideturtle()

width = 100
height = 280
radius = 30

t.penup()
t.goto(-width / 2, height / 2)
t.pendown()

t.begin_fill()
for _ in range(4):
    t.forward(width if _ % 2 == 0 else height)
    t.right(90)
t.end_fill()

colors = ['#ed1c24', '#ffff00', '#00ff00']

for _ in range(3):
    t.penup()
    # t.goto(0, height / 2 - radius * 2 * (_ + 1) - (height / 2 - radius * 2) / 4 * (_ + 1))
    t.goto(0, height / 2 - radius * 2 * (_ + 1) - (height - (radius * 2 * 3)) / 4 * (_ + 1))

    t.pendown()
    t.pencolor(colors[_])
    t.fillcolor(colors[_])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

t.exitonclick()