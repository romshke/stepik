import turtle

window = turtle.Screen()

def square(side):
    angle = -15

    for _square in range(3):
        angle += 30

        for _side in range(4):
            turtle.setheading(angle + 90 * _side)
            turtle.forward(side)

square(int(input()))

window.exitonclick()