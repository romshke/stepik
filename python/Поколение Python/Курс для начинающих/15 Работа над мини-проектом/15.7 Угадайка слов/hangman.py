# Описание проекта: программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова неизвестны. Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово. Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове. Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову. Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово. За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.

from random import choice


word_list = ['постановление', 'руководитель', 'мать', 'строй', 'офицер', 'препарат', 'множество', 'перспектива', 'мнение', 'расчет', 'власть', 'озеро', 'хвост', 'ухо', 'самолет', 'работник', 'сезон', 'пункт', 'оценка', 'опасность']

def get_word(word_list):
    return choice(word_list)

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def get_indexes(letter, word):
    indexes = list()

    for index, symbol in enumerate(word):
        if symbol == letter: indexes.append(index)

    return indexes

def play(word, is_first_game):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    word = word.upper()

    if is_first_game:
        print('Давайте играть в угадайку слов!')

    print(display_hangman(tries), word_completion, sep='\n')

    while tries > 0 and not guessed:
        input_string = input().upper()

        if input_string.isalpha():
            if len(input_string) == 1:
                if input_string not in guessed_letters:
                    guessed_letters.append(input_string)

                    if word.count(input_string) == 1:
                        index = word.index(input_string)
                        word_completion = word_completion[:index] + input_string + word_completion[index + 1:]
                    elif word.count(input_string) > 1:
                        indexes = get_indexes(input_string, word)
                        for index in indexes:
                            word_completion = word_completion[:index] + input_string + word_completion[index + 1:]
                    else:
                        tries -= 1
                        print(display_hangman(tries))
                else:
                    print('Вы уже вводили данную букву ранее')
            elif len(input_string) == len(word):
                if input_string not in guessed_words:
                    guessed_words.append(input_string)

                    if input_string == word:
                        word_completion = input_string
                        guessed = True
                    else:
                        tries -= 1
                else:
                    print('Вы уже вводили данное слово ранее')
            else:
                print('Некорректный ввод! Введите букву или слово целиком.')
        else:
            print('Некорректный ввод! Введите букву или слово целиком.')

        print(display_hangman(tries), word_completion, sep='\n')
        
        if word_completion == word:
            guessed = True
    else:
        pass
        
    print('Поздравляем, вы угадали слово! Вы победили!') if guessed else print(f'Вы исчерпали все попытки! Вам было загадано слово {word}')

try_again = True
is_first_game = True

while try_again:
    reply = str()

    play(get_word(word_list), is_first_game)
    print('Хотите сыграть еще раз? Введите да или нет')
    while reply != 'нет' and reply != 'да':
        reply = input().lower().strip()

        if reply != 'нет' and reply != 'да':
            print('Введите да или нет')
    
    if reply == 'нет':
        try_again = False 
    if reply == 'да':
        is_first_game = False


# Улучшения проекта

# Можно отображать первую и последнюю букву слова;

# Слова можно выделить в категории и давать подсказку пользователю;

# Существует также вариант игры с 8 частями — добавляются ступни, а также самый длинный вариант, когда сначала за не отгаданную букву рисуются части самой виселицы.