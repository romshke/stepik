import turtle

turtle.speed(20)
turtle.shape('turtle')
# turtle.shapesize(2)
turtle.penup()
i = 0

for _ in range(40):
    turtle.right(20)
    turtle.forward(i)
    i += 1
    if i % 2 == 0:
        turtle.stamp()

turtle.exitonclick()