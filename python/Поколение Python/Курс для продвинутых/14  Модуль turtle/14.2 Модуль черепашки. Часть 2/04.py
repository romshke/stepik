import turtle

turtle.speed(20)

def web(length):
    for _ in range(8):
        turtle.pensize(12)
        turtle.dot()
        turtle.pensize(3)
        turtle.forward(length)
        turtle.shapesize(3)
        turtle.stamp()
        turtle.pensize(3)
        turtle.backward(length)
        turtle.setheading(360/8 * (_ + 1))
    
    turtle.shapesize(1)
    turtle.shape('circle')

web(200)

turtle.exitonclick()