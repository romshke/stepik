age = int(input())

if age < 14:
    print('детство')
elif age >= 14 and age <= 24:
    print('молодость')
elif age >= 25 and age <= 59:
    print('зрелость')
else:
    print('старость')