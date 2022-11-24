t, r = input(), input()

def who_win(first, second):
    match first:
        case 'камень':
            match second:
                case 'камень': return 0
                case 'ножницы': return 1
                case 'бумага': return 2
                case 'ящерица': return 1
                case 'Спок': return 2
        case 'ножницы':
            match second:
                case 'камень': return 2
                case 'ножницы': return 0
                case 'бумага': return 1
                case 'ящерица': return 1
                case 'Спок': return 2
        case 'бумага':
            match second:
                case 'камень': return 1
                case 'ножницы': return 2
                case 'бумага': return 0
                case 'ящерица': return 2
                case 'Спок': return 1
        case 'ящерица':
            match second:
                case 'камень': return 2
                case 'ножницы': return 2
                case 'бумага': return 1
                case 'ящерица': return 0
                case 'Спок': return 1
        case 'Спок':
            match second:
                case 'камень': return 1
                case 'ножницы': return 1
                case 'бумага': return 2
                case 'ящерица': return 2
                case 'Спок': return 0

print('Тимур' if who_win(t, r) == 1 else ('Руслан' if who_win(t, r) == 2 else 'ничья'))