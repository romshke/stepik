# объявление функции
def draw_box():
    for _ in range(14):
        if _ == 0 or _ == 13: print('*' * 10)
        else: print(f'*{" " * 8}*')

# основная программа
draw_box()  # вызов функции