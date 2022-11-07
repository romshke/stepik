s = input()
count = 0

for _ in range(1, len(s)):
    if s[_] == s[_ - 1]:count += 1
print(count)
