# объявление функции
def find_all(target, symbol):
    return list(i for i, _ in enumerate(target) if _ == symbol)

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))