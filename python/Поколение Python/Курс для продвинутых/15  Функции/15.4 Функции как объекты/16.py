def f(number):
    return sum(map(int, number))
    
numbers = input().split()

print(*sorted(sorted(numbers, key=int), key=f))