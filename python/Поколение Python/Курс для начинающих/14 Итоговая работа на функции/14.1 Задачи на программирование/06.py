# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

def factorial(n):
    result = 1
    for _ in range(1, n + 1): result *= _

    return result

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))