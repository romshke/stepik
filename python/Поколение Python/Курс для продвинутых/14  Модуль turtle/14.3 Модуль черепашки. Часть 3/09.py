from math import radians, tan
from random import choice, randint
import string
import turtle as t

t.hideturtle()
# t.tracer(6, 0)
t.speed(10)

# a = 50
# print(s)

def get_side(s, n = 3):
    return (s * 4 * tan(radians(180) / n) / n)**0.5

def figure(n=3, a=50):
    
    color = '#' + ''.join([(choice(string.hexdigits)) for _ in range(6)]) # случайный hex цвет 
    t.fillcolor(color)

    t.begin_fill()

    for _ in range(n):
        t.forward(a)
        t.right(360 / n)

    t.end_fill()

s = 2500

for raw in range(5):
    t.penup(), t.sety(300 - 100*raw), t.pendown()
    for column in range(5):
        n = randint(3, 7)
        t.penup(), t.setx(-300 + 100*column), t.pendown()
        figure(n, get_side(s, n))
        

        
        

t.exitonclick()