# объявление функции
def is_palindrome(text):
    return True if text.lower().translate({ord(_): None for _ in ' ,.!?-'}) == text.lower().translate({ord(_): None for _ in ' ,.!?-'})[::-1] else False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))