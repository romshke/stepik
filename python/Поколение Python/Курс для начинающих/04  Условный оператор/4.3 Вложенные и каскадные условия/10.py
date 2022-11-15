x = int(input())

if x == 0: print("зеленый")
elif x >= 1 and x <= 10:
    if x % 2 == 0: print("черный")
    else: print("красный")
elif x >= 11 and x <= 18:
    if x % 2 == 0: print("красный")
    else: print("черный")
elif x >= 19 and x <= 28:
    if x % 2 == 0: print("черный")
    else: print("красный")
elif x >= 29 and x <= 36:
    if x % 2 == 0: print("красный")
    else: print("черный")
else: print("ошибка ввода")