import turtle

turtle.speed(10)

for line in range(10):
    turtle.pendown()
    turtle.pencolor('cyan')
    turtle.goto(-180 + (line * 40), -200)
    turtle.dot('blue')
    turtle.penup()
    turtle.goto(0, 0)

turtle.dot('red')
     
turtle.exitonclick()