# объявление функции
def get_factors(num):
    return list(_ for _ in range(1, num + 1) if num % _ == 0)

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))