# объявление функции
def is_password_good(password):
    upper = False
    lower = False
    num = False

    if len(password) < 8: return False
    
    for _ in password:
        if _.isdigit(): num = True
        if _.islower(): lower = True
        if _.isupper(): upper = True

    if upper and lower and num: return True
    else: return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))