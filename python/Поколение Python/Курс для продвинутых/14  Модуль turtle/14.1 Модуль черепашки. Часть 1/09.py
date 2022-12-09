import turtle

turtle.speed(20)

def rhombus(side):
    angle = 0
    
    # for _rhombus in range(12):
    for _rhombus in range(10):
        
        
        for _side in range(4):
            turtle.setheading(angle)
            turtle.forward(side)
            
            if _side % 2 == 0:
                angle -= 60
            else:
                angle -= 120
        
        # angle = 30 * (_rhombus + 1)
        angle = 35 * (_rhombus + 1)
        
rhombus(200)

turtle.exitonclick()