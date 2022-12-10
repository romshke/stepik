import turtle as t

t.speed(10)
t.hideturtle()
t.pensize(3)
side = 200

t.fillcolor('#00a2e8')
t.begin_fill()

for _ in range(4):
    t.forward(side)
    t.right(90)
    
t.end_fill()

t.backward(side * 0.3)
t.fillcolor('#b97a57')
t.begin_fill()
t.goto(-0.3 * side, 0)
t.goto(1.3 * side, 0)
t.goto(side / 2, side)
t.goto(-0.3 * side, 0)
t.end_fill()
    
t.exitonclick()