import turtle

turtle.speed(20)

def star(length):
    for side in range(5):
        turtle.forward(length)
        turtle.setheading(-144 * (side + 1))
        
star(200)

turtle.exitonclick()