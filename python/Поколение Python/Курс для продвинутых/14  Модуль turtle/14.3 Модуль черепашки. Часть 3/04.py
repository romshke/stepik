import turtle as t

def triangle(side, direction, flag = False, pencolor = '#000000'):
    t.pensize(3)
    t.pencolor(pencolor)
    
    for _ in range(3):
        if flag:
            t.penup()
            print_dot(30)
            
        t.forward(side)
        direction(120)
        
    t.pendown()
    
def print_dot(pensize):
    t.pensize(pensize)
    t.dot()
    t.pensize(1)

side = 200
height = (side**2 - (side / 2)**2)**0.5

t.penup()
t.goto(-side/2, -height/2)
t.pendown()

triangle(side, t.left, None)

t.penup()
t.goto(-side/2, -height/2 + 2*height/3)
t.pendown()

triangle(side, t.right, True, '#000000')

t.fillcolor('#ffffff')
t.begin_fill()
triangle(side, t.right, False, '#ffffff')
t.end_fill()

t.exitonclick()