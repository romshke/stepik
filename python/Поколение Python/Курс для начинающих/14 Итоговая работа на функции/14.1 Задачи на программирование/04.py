# объявление функции
def draw_triangle():
    i = 0
    for _ in range(1, 9):
        print(' ' * ((15 // 2) - i) + '*' * (_ + i))
        i += 1

# основная программа
draw_triangle()  # вызов функции