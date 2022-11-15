s = input()
count_plus, count_star = 0, 0

for _ in s:
    if _ == '+': count_plus += 1
    if _ == '*': count_star += 1
print(f"Символ + встречается {count_plus} раз\nСимвол * встречается {count_star} раз")
