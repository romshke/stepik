# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

def is_encription():
    while True:
        print('Выберите режим шифрование или дешифрование. Ввведите шифрование / дешифрование (encryption / decryption)')

        input_string = input().lower().strip()

        if input_string == 'шифрование' or input_string == 'encryption':
            return True
        elif input_string == 'дешифрование' or input_string == 'decryption':
            return False
        else:
            print('Ввведите шифрование / дешифрование (encryption / decryption')

def get_shift(is_encription = True):
    while True:
        print('Введите шаг сдвига')

        try:
            shift = int(input())
            if shift >= 0:
                return shift if is_encription else -shift
            else:
                print('Введите корректное число')
        except:
            print('Введите корректное число')           

def caesar_cipher(shift = 0, input_string = ''):
    result = str()

    if input_string == '':
        input_string = input()

    for _ in input_string:
        if _.isalpha():
            if ord('A') <= ord(_) <= ord('Z'):
                result += chr(ord('A') + (ord(_) - ord('A') + shift) % 26)
            if ord('a') <= ord(_) <= ord('z'):
                result += chr(ord('a') + (ord(_) - ord('a') + shift) % 26)
            if ord('А') <= ord(_) <= ord('Я'):
                result += chr(ord('А') + (ord(_) - ord('А') + shift) % 32)
            if ord('а') <= ord(_) <= ord('я'):
                result += chr(ord('а') + (ord(_) - ord('а') + shift) % 32)
        else:
            result += _
    
    return result

print(caesar_cipher(get_shift(is_encription())))
    
# for _ in range(0, 26):
# print(caesar_cipher(1))
