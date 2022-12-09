import turtle

turtle.speed(20)

def rays(length):
    for ray in range(12):
        turtle.setheading(30 * ray)
        turtle.forward(length)
        turtle.backward(length)
        
rays(200)

turtle.exitonclick()