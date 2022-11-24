result = list()
n = int(input())

for _ in range(n):
    s = input()

    if s.find('a') < s.find('n', s.find('a')) < s.find('t', s.find('n', s.find('a'))) < s.find('o', s.find('t', s.find('n', s.find('a')))) < s.find('n', s.find('o', s.find('t', s.find('n', s.find('a'))))):
        result.append(_ + 1)

print(*result)