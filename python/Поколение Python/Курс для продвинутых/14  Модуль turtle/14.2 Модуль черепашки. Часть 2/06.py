import turtle

turtle.speed(20)
turtle.shape('turtle')
turtle.shapesize(2)
turtle.pensize(6)

def watch(length):
    for _ in range(12):
        turtle.penup()
        turtle.forward(length * 0.75)
        turtle.pendown()
        turtle.forward(length * 0.1)
        turtle.penup()
        turtle.forward(length * 0.15)
        turtle.stamp()
        turtle.backward(length)
        turtle.setheading(360/12 * (_ + 1))

watch(200)

turtle.exitonclick()