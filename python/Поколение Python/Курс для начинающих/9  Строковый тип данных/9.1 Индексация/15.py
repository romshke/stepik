n = int(input())
result = ''

while n > 0:
    result += str(n % 2)
    n //= 2

print(result[::-1])