import turtle
window = turtle.Screen()

def triangle(side):
    turtle.forward(side)
    turtle.setheading(120)

    turtle.forward(side)
    turtle.setheading(240)

    turtle.forward(side)
    
triangle(int(input()))

window.exitonclick()
