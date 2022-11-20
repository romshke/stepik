# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.

def caesar_cipher(input_string = ''):
    result = str()
    words_and_delimiters = list()
    word = str()

    if input_string == '':
        input_string = input()

    for _ in input_string:
        if _.isalpha():
            word += _
        elif not _.isalpha() and word != '':
            words_and_delimiters.append(word)
            words_and_delimiters.append(_)
            word = ''
        else:
            words_and_delimiters.append(_)
    
    if word != '':
        words_and_delimiters.append(word)
        word = ''

    for item in words_and_delimiters:
        if item.isalpha():
            for _ in item:
                if ord('A') <= ord(_) <= ord('Z'):
                    result += chr(ord('A') + (ord(_) - ord('A') + len(item)) % 26)
                if ord('a') <= ord(_) <= ord('z'):
                    result += chr(ord('a') + (ord(_) - ord('a') + len(item)) % 26)
        else:
            result += item

    return result

print(caesar_cipher())