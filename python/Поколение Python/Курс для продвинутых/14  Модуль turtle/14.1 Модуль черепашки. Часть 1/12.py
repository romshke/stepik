import turtle

turtle.speed(20)

def pattern(length):
    for square in range(35):
        for side in range(4):
            turtle.setheading(90 * (side + 1))
            turtle.forward(length - (5 * square))
        
pattern(200)

turtle.exitonclick()