from random import choice, randint
import string
import turtle as t

width, height = 600, 600
t.Screen().setup(width, height)
t.hideturtle()
t.tracer(12, 0)

def star():
    side = randint(10, 30)
    color = '#' + ''.join([(choice(string.hexdigits)) for _ in range(6)]) # случайный hex цвет 
    x, y = randint(-width/2 + side, width/2 - side), randint(-height/2 + side, height/2 - side)
    
    t.penup(), t.goto(x, y), t.pendown()
    t.right(randint(0, 360)) # случайный начальный поворот
    t.pencolor(color), t.fillcolor(color)
    
    t.begin_fill()
    
    for _ in range(5):
        t.forward(side)
        t.right(144)

    t.end_fill()
    
for _ in range(200): star()

t.exitonclick()