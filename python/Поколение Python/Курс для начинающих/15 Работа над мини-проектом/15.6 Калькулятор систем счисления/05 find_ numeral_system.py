def n_to_dec(base, number):
    result = 0

    for i, _ in enumerate(str(number)[::-1].upper()):
        if _.isdigit():
            result += int(_) * (base**i)
        else:
            match _:
                case 'A': result += 10 * (base**i)
                case 'B': result += 11 * (base**i)
                case 'C': result += 12 * (base**i)
                case 'D': result += 13 * (base**i)
                case 'E': result += 14 * (base**i)
                case 'F': result += 15 * (base**i)
    
    return result
    
for _ in (9, 16):
    if n_to_dec(_, 88) == n_to_dec(_, 32) + n_to_dec(_, 22) + n_to_dec(_, 16) + n_to_dec(_, 17):
        print(_)
