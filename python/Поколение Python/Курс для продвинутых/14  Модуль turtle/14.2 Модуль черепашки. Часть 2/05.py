import turtle

turtle.speed(20)
turtle.shape('turtle')
turtle.shapesize(3)

def web(length):
    for _ in range(10):
        turtle.penup()
        turtle.forward(length)
        turtle.stamp()
        turtle.backward(length)
        turtle.setheading(360/10 * (_ + 1))

web(200)

turtle.exitonclick()