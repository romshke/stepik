# объявление функции
def is_correct_bracket(text):
    count = 0

    for _ in text:
        if _ == '(': count += 1
        if _ == ')': count -= 1
        if count == -1: return False
    
    return True if count == 0 else False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))