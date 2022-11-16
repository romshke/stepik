# # объявление функции
# def number_to_words(num):
    
#     if num < 20:
#         return from_1_to_19(num)
#     else:
#         result = ''
#         n = str(num)

#         match n[0]:
#             case '2': result = 'двадцать'
#             case '3': result = 'тридцать'
#             case '4': result = 'сорок'
#             case '5': result = 'пятьдесят'
#             case '6': result = 'шестьдесят'
#             case '7': result = 'семьдесят'
#             case '8': result = 'восемьдесят'
#             case '9': result = 'девяносто'

#         if int(n[1]) == 0: return result
#         else: return f"{result} {from_1_to_19(int(n[1]))}"
    
# def from_1_to_19(num):
#     match num:
#         case 1: return 'один'
#         case 2: return 'два'
#         case 3: return 'три'
#         case 4: return 'четыре'
#         case 5: return 'пять'
#         case 6: return 'шесть'
#         case 7: return 'семь'
#         case 8: return 'восемь'
#         case 9: return 'девять'
#         case 10: return 'десять'
#         case 11: return 'одиннадцать'
#         case 12: return 'двенадцать'
#         case 13: return 'тринадцать'
#         case 14: return 'четырнадчать'
#         case 15: return 'пятнадцать'
#         case 16: return 'шестнадцать'
#         case 17: return 'семнадцать'
#         case 18: return 'восемнадцать'
#         case 19: return 'девятнадцать'

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_to_words(n))


# объявление функции
def number_to_words(num):
    list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if num <= 10: return list_1[num - 1]
    elif 11 <= num <= 19: return list_11[num - 11]
    else:
        if str(num)[1] == '0': return list_21[int(str(num)[0]) - 2]
        else: return f'{list_21[int(str(num)[0]) - 2]} {list_1[int(str(num)[1]) - 1]}'

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))