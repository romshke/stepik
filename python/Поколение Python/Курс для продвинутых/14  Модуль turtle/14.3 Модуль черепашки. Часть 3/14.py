import random
import turtle as t

s_width, s_height = 500, 500

t.Screen().setup(s_width, s_height)
t.Screen().bgcolor('#001e42')

# t.hideturtle()
# t.speed(0)

def set_buildings(s_width, s_height):
    widths = range(int(s_width*0.06), int(s_width*0.2) + 1, int(s_width*0.02))
    heights = range(int(s_height*0.2), int(s_height*0.9) + 1, int(s_height*0.04))
    
    result = []
    
    while sum(map(lambda _: _[0], result)) < s_width:
        width = random.choice(widths)
        height = random.choice(heights) - s_height//2
        
        if sum(map(lambda _: _[0], result)) + width > 500:
            width = s_width - sum(map(lambda _: _[0], result))
            
        result.append((width, height))
       
    print(result, sum(map(lambda _: _[0], result)))
        
    return result

def buildings(widths_heights, s_height):
    t.penup(), t.goto(-s_width/2, -s_height/2), t.pendown()
    t.pencolor('#0243a0')
    t.fillcolor('#0243a0')
    
    t.begin_fill()
    for width, height in widths_heights:
        t.goto(t.xcor(), height)
        t.goto(t.xcor() + width, height)
        
    t.goto(t.xcor(), -s_height//2)
    
    t.end_fill()

def windows(widths_heights):
    t.pencolor('#fffc8a')
    t.fillcolor('#fffc8a')
    
    for window in range(20):
        t.penup(), t.goto(-240 + 25 * window, -200), t.pendown()
        
        t.begin_fill()
        for side in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()
    


def stars():
    pass


widths_heights = set_buildings(s_width, s_height)


buildings(widths_heights, s_height)
windows(widths_heights)



t.exitonclick()