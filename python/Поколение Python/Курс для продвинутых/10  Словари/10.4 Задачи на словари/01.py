my_dict = {}

for _ in range(int(input())):
    data = input().split(': ')
    my_dict.setdefault(data[0].lower(), data[1])
    
for _ in range(int(input())):
    word = input().lower()
    print(my_dict[word] if word in my_dict else 'Не найдено')