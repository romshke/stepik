# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

from random import randint, choice

def is_right_border_valid(input_string):
    try:
        if int(input_string) > 1: return True
        else: return False
    except:
        return False

def generate_number(right_border):
    return randint(1, right_border)

def is_number_valid(input_string, right_border):
    try:
        if 1 <= int(input_string) <= right_border: return True
        else: return False
    except:
        return False

def guess_number(number_2_guess, number):
    less_responses = ['Слишком мало, попробуйте еще раз', 'Ваше число меньше загаданного, попробуйте еще разок']
    more_responses = ['Слишком много, попробуйте еще раз', 'Ваше число больше загаданного, попробуйте еще разок']

    if number_2_guess > number: return False, choice(less_responses)
    elif number_2_guess < number: return False, choice(more_responses)
    else: return True, 'Вы угадали, поздравляем!'

def new_game():
    right_border, number_2_guess, number = int(), int(), int()
    guess_counter = 0

    print('Укажите правую границу диапазона: целое число больше 1')

    # Ввод правой границы диапазона и генерация угадываемого числа 
    while True:
        input_string = input()

        if is_right_border_valid(input_string):
            right_border = int(input_string)
            number_2_guess = generate_number(right_border)
            break
        else: print('Введите целое число больше 1')

    # print(right_border, number_2_guess)
            
    print(f'Введите число от 1 до {right_border}')

    while True:
        input_string = input() 

        if is_number_valid(input_string, right_border):
            number = int(input_string)
            is_guessed, response = guess_number(number_2_guess, number)

            # Защитываются только попытки внутри диапазона
            guess_counter += 1

            if is_guessed:
                print(response, f'Вы угадали число с {guess_counter} попытки', sep='\n')
                break
            else:
                print(response)
        else: print(f'А может быть все-таки введем целое число от 1 до {right_border}?')    

def game():
    play_again = True

    print('Добро пожаловать в числовую угадайку')

    while play_again:
        new_game()

        print('Хотите сыграть снова?')

        while True:
            print('Введите да, чтобы повторить или нет, чтобы закончить игру')

            input_string = input().lower().strip()

            if input_string == 'да':
                break
            elif input_string == 'нет':
                play_again = False
                break
            else: continue
        
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

game()