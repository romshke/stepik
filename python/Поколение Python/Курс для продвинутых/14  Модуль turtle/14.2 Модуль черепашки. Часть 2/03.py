import turtle

turtle.speed(20)

def rectangle(width, height):
    for _ in range(4):
        turtle.pensize(12)
        turtle.dot()
        turtle.pensize(3) 
        turtle.forward(width if _ % 2 == 0 else height)
        turtle.setheading(-90 * (_ + 1))
        
    turtle.shape('circle')

rectangle(400, 200)

turtle.exitonclick()