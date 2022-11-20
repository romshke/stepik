def BOH(number): 
    return bin(number)[2:], oct(number)[2:], hex(number)[2:].upper()

print(*BOH(int(input())), sep='\n')