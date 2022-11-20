def hex_2_dec(hex_num):
    result = 0

    for i, _ in enumerate(hex_num[::-1].upper()):
        if _.isdigit():
            result += int(_) * (16**i)
        else:
            match _:
                case 'A': result += 10 * (16**i)
                case 'B': result += 11 * (16**i)
                case 'C': result += 12 * (16**i)
                case 'D': result += 13 * (16**i)
                case 'E': result += 14 * (16**i)
                case 'F': result += 15 * (16**i)
    
    return result

print(hex_2_dec(input()))