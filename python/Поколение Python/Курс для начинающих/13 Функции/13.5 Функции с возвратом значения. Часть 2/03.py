# объявление функции
def is_prime(num):
    result = True

    if num == 1: return False
    
    for _ in range(2, num):
        if num % _ == 0:
            result = False
            break
    return result

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))