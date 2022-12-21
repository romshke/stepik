from math import cos, radians, sin
import turtle as t

def ellipse(a, b):
    dx = t.xcor()
    dy = t.ycor()
    for deg in range(361):
        rad = radians(deg)
        x = a * sin(rad) + dx
        y = -b * cos(rad) + b + dy
        t.goto(x, y)

radiuses = [100, 25, 40, 25, 20, 60, 60, 40, 38, 10]
titles = ['Солнце', 'Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун', 'Плутон']
colors = ['#fffc8a', '#e5bd57', '#e5bd57', '#96eec9', '#fc8165', '#e5bd57', '#e5bd57', '#6fc6dd', '#0aa2ff', '#e5bd57']

t.hideturtle()
# t.speed(0)
t.tracer(12, 0)
# t.Screen().setup(1000, 500)

x = -(sum(radiuses) + 15 * 9 + 20)

for radius, title, color in zip(radiuses, titles, colors):
    x += radius
    t.penup(), t.goto(x, -radius), t.pendown()
    t.fillcolor(color), t.begin_fill(), t.circle(radius), t.end_fill()
    t.penup(), t.goto(x, -radius - 20), t.write(title, align='center'), t.pendown()
    if title == 'Юпитер': x += 20
    if title == 'Сатурн':
        t.penup(), t.goto(x, -radius//1.4), t.pendown()
        ellipse(radius + 20, radius//1.4)
        x += 20
    x += radius + 30
    

 
 

    
t.exitonclick()
