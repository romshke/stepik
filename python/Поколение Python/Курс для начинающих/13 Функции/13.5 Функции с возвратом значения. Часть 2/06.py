# объявление функции
def is_one_away(word1, word2):
    count = 0

    for _ in range(len(word1)):
        if word1[_] != word2[_]: count += 1
        if count > 1:
            break
        
    return True if len(word1) == len(word2) and count == 1 else False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))