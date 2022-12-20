import turtle as t

t.hideturtle()

line = 200

pt_2_px = lambda pt: -pt/2*1.333

t.setx(-line/2)
t.penup(), t.sety(pt_2_px(12)), t.setx(-line/2 - 10), t.write('Запад', align='right', font=(12)), t.goto(-line/2, 0), t.pendown()

t.setx(line/2)
t.penup(), t.sety(pt_2_px(12)), t.setx(line/2 + 10), t.write('Восток', align='left', font=(12)), t.goto(line/2, 0), t.pendown()

t.setx(0)
t.sety(line/2)
t.penup(),  t.sety(line/2 + 10), t.write('Север', align='center', font=(12)), t.goto(0, line/2), t.pendown()

t.setx(0)
t.sety(-line/2)
t.penup(), t.sety(-line/2 - 10 + pt_2_px(12) * 2), t.write('Юг', align='center', font=(12)), t.goto(0, line/2), t.pendown()

t.sety(-line/8)
t.circle(line/8)

t.exitonclick()