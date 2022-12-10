import turtle

turtle.pensize(20)

def dots(count):
    turtle.penup()
    turtle.backward((count // 2) * 50)
    turtle.pendown()
    
    for _ in range(count):
        turtle.dot()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

dots(11)

turtle.exitonclick()