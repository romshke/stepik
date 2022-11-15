color1, color2 = input(), input()

if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный": print("фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный": print("оранжевый")
elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий": print("зеленый")
elif color1 == color2 == "красный" or color1 == color2 == "синий" or color1 == color2 == "желтый": print(color1)
else: print("ошибка цвета")