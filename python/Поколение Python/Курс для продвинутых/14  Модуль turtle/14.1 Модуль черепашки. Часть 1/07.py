import turtle

turtle.speed(20)

def hexagon(side):
    angle = 0
    
    for _hexagon in range(6):
        turtle.setheading(angle)
        
        for _side in range(6):
            turtle.forward(side)
            turtle.setheading(angle - 60 * (_side + 1))

        turtle.forward(side)
        angle += 60

hexagon(100)

turtle.exitonclick()