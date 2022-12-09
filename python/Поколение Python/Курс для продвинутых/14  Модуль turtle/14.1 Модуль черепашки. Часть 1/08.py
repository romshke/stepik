import turtle

turtle.speed(5)

def rhombus(side):
    angle = -60
    
    for _side in range(4):
        turtle.forward(side)
        turtle.setheading(angle)
        
        if _side % 2 == 0:
            angle -= 120
        else:
            angle -= 60
        
rhombus(100)

turtle.exitonclick()