number = int(input())
_number = number
divisor = 2
flag = True

while _number > 1:
    if divisor > 5:
        flag = False
        break
    
    if _number % divisor == 0:
        # print(_number, divisor)
        _number //= divisor
    else: divisor += 1
    
print('YES' if flag and number > 1 else 'NO')