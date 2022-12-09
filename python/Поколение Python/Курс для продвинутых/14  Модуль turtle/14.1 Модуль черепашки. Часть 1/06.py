import turtle

turtle.speed(20)

def hexagon(side):
    for _side in range(6):
        turtle.forward(side)
        turtle.setheading(60 * (_side + 1))
    
hexagon(100)

turtle.exitonclick()