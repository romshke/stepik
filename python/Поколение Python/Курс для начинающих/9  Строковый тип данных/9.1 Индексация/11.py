s = input()

for _ in s:
    try:
        if int(_):
            print('Цифра')
            break
    except:
        continue     
else: print('Цифр нет')