def pascal(n):
    result = list()

    if n == 0:
        result = [1]
    elif n == 1:
        result = [1, 1]
    else:
        previous_line = pascal(n - 1)
        for i in range(n+1):
            if i == 0 or i == n:
                result.append(1)
            else:
                result.append(sum(previous_line[i - 1:i + 1]))
    
    return result

print(pascal(int(input())))