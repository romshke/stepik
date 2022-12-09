import turtle

turtle.speed(20)

def square(side):
    angle = -45

    for _square in range(8):
        angle += 45

        for _side in range(4):
            turtle.setheading(angle + 90 * _side)
            turtle.forward(side)
            
# square(int(input()))
square(100)

turtle.exitonclick()