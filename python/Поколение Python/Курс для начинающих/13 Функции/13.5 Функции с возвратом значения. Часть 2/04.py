# объявление функции
def get_next_prime(num):
    flag = True
    i = 1

    while flag:
        for _ in range(2, num + i):
            if (num + i) % _ == 0: break
        else:
            flag = False
            break 
        i += 1

    return num + i

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))