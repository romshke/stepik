def f(number):
    return sum(map(int, number))

numbers = input().split()

print(*sorted(numbers, key=f))