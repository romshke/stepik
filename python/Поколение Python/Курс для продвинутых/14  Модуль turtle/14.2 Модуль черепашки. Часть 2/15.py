import turtle as t
from random import choice

t.speed(0)
t.bgcolor('#00ffff')
t.Screen().screensize(600, 600)

def snowflakes(radius, color):
    t.setheading(0)
    t.pencolor(color)
    t.pensize(6)
    t.dot()
    t.pensize(3)
    t.pendown()
    
    for line in range(8):
        t.setheading(360 / 8 * line)
        
        for _ in range(4):
            if _ < 3:
                t.forward(radius / 4)
                
                t.left(45)
                t.forward(radius / 4)
                t.backward(radius / 4)
                
                t.right(90)
                t.forward(radius / 4)
                t.backward(radius / 4)
                
                t.left(45)
            else:
                t.forward(radius / 4)
                t.backward(radius)
    
    t.penup()

colors = ['#e80af3', '#7e0381', '#020bfe', '#7e0481', '#7e7d80']

for snowflake in range(5):
    radius = choice(range(40, 101, 20))
    snowflakes(radius, colors[snowflake])
    sign = (-1 if snowflake % 2 == 0 else 1)
    
    if snowflake < 2:
        x = -250 
        y = -250 * sign
        t.goto(x, y)
    else:
        x = 250 
        y = 250 * sign
        t.goto(x, y)
    
t.exitonclick()