import turtle as t

t.speed(0)

def figure(n=8, side=50):
    for _ in range(n):
        t.forward(side)
        t.right(360 / n)
        
t.penup(), t.goto(-50, (100**2/2)**0.5 + 50), t.pendown()

t.fillcolor('red'), t.begin_fill()
figure(side=100)
t.end_fill()

t.pencolor('white')
t.pensize(15)
figure(side=100)

t.pencolor('black')
t.pensize(5)
figure(side=100)

t.penup(), t.goto(0, -(100**2/2)**0.5 + 20), t.pendown()

t.color('white')
t.write('STOP', align='center', font=['Arial', 60, 'bold'])

t.exitonclick()
    

