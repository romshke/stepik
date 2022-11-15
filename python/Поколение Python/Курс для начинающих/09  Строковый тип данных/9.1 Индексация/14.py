s = input()
vovels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
count_vovels = 0
count_consonants = 0

for _ in s:
    if _ in vovels: count_vovels += 1
    if _ in consonants: count_consonants += 1
print(f"Количество гласных букв равно {count_vovels}\nКоличество согласных букв равно {count_consonants}")
