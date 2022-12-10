import turtle

turtle.speed(10)
turtle.pensize(3)

def star(side_len):
    turtle.goto(-side_len / 2, 0)
    
    sign = 1
    
    for triangle in range(2):
        if triangle == 1:
            sign = -1
            turtle.goto(-side_len / 2, side_len * 0.55)
            turtle.pendown()
            
        for side in range(3):
            turtle.forward(side_len)
            turtle.left(120 * sign)

        turtle.penup()
        
star(300)
        
turtle.exitonclick()