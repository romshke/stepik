# объявление функции
def is_valid_password(password):
    l = password.split(':')
    a, b, c = l[0], l[1], l[2]

    return len(l) == 3 and a == a[::-1] and (True if len(list(_ for _ in range(2, int(b)) if int(b) % _ == 0)) == 0 else False) and int(c) % 2 == 0

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))