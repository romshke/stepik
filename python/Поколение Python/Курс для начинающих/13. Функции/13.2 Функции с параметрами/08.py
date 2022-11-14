# объявление функции
def draw_triangle(fill, base):
    for _ in range((base + 1) // 2): print(fill * (_  + 1))
    for _ in range((base + 1) // 2, base): print(fill * (base - _))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)