import turtle

turtle.speed(20)

def pattern(length):
    angle = -90
     
    for square in range(40):
        for side in range(2):
            turtle.setheading(angle)
            turtle.forward(length - (length * 0.025 * square))
            angle -= 90

pattern(300)

turtle.exitonclick()