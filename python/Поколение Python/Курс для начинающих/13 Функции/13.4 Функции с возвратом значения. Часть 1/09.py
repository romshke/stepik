# объявление функции
def number_of_factors(num):
    return len(list(_ for _ in range(1, num + 1) if num % _ == 0))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))