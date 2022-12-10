import turtle

colors = ['blue', 'yellow', 'green', 'purple', 'orange', 'red']

turtle.speed(10)
length = 10
pen_size = 2

for _ in range(68):
    if _ % 2 == 0:
        turtle.pensize(pen_size)
        length *= 1.1
        pen_size *= 1.1
    
    turtle.pencolor(colors[_ % 6])
    turtle.left(45)
    turtle.forward(length)

        
turtle.exitonclick()