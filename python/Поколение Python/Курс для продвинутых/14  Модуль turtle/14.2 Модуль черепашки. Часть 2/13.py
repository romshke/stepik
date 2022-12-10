import turtle

colors = ['#00f900', 'red', 'black', '#5cddff', 'yellow']
turtle.speed(10)
turtle.pensize(5)
turtle.penup()
turtle.goto(30, -60)
turtle.pendown()


for _ in range(5):
    if 0 < _ < 4:
        turtle.penup()
        turtle.goto(80 - 105 * (_ - 1), 0)
        turtle.pendown()
    elif _ > 3:
        turtle.penup()
        turtle.goto(-75, -60)
        turtle.pendown() 
        
    turtle.pencolor(colors[_])
    turtle.circle(50)
     
turtle.exitonclick()