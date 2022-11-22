def zodiac(year):
    match year:
        case 8: return 'Дракон'
        case 9: return 'Змея'
        case 10: return 'Лошадь'
        case 11: return 'Овца'
        case 0: return 'Обезьяна'
        case 1: return 'Петух'
        case 2: return 'Собака'
        case 3: return 'Свинья'
        case 4: return 'Крыса'
        case 5: return 'Бык'
        case 6: return 'Тигр'
        case 7: return 'Заяц'

print(zodiac(int(input()) % 12))