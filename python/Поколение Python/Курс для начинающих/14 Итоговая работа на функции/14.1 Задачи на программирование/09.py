# объявление функции
def is_magic(date):
    l = date.split('.')

    return True if (int(l[2][-2:]) == int(del_zeros(l[0])) * int(del_zeros(l[1]))) else False

def del_zeros(n):
    if n[0] == '0': return n[1]
    else: return n

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))