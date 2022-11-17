# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

from random import choice

def yes_no_checker():
    reply_string = ''

    while not (reply_string == 'да' or reply_string == 'нет'):
        reply_string = input().lower().strip()
        
        if not (reply_string == 'да' or reply_string == 'нет'): print('Введите да или нет')

    return True if reply_string == 'да' else False

def int_checker():
    number = int()
    while True:
        try:
            number = int(input().strip())
            if number > 0: break
            else: print('Введите корректное число')
        except:
            print('Введите корректное число')

    return number

def generate_password(length, chars):
    password = ''

    for _ in range(length):
        password += choice(chars)
    
    return password

def secure_password_generator():
    digits = '0123456789'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '!#$%&*+-=?@^_'
    passwords_count, password_length, passwords = int(), int(), list()
    chars = ''

    print('Введите количество генерируемых паролей')
    passwords_count = int_checker()

    print('Введите количество символов в одном пароле')
    password_length = int_checker()

    print('Включать ли цифры 0123456789 в пароль? Введите да или нет')
    if yes_no_checker(): chars += digits

    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ в пароль? Введите да или нет')
    if yes_no_checker(): chars += uppercase_letters

    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz в пароль? Введите да или нет')
    if yes_no_checker(): chars += lowercase_letters

    print('Включать ли символы !#$%&*+-=?@^_ в пароль? Введите да или нет')
    if yes_no_checker(): chars += punctuation

    print('Исключать ли неоднозначные символы il1Lo0O? Введите да или нет')
    if yes_no_checker():
        for _ in 'il1Lo0O': chars = chars.replace(_, '')

    for _ in range(passwords_count):
        passwords.append(generate_password(password_length, chars))

    return passwords

for _ in secure_password_generator():
    print(_)