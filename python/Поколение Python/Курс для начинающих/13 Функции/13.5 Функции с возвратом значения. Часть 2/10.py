# объявление функции
def convert_to_python_case(text):
    result = ''
    i = 0

    while text != '':
        if i + 1 == len(text):
            result += text.lower()
            text = text.replace(text, '')
        elif text[i + 1].isupper():
            result += text[:i + 1].lower() + '_'
            text = text.replace(text[:i + 1], '')
            i = 0
        i += 1

    return result 

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))