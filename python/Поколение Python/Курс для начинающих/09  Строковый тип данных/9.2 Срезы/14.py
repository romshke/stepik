s = input()

# if len(s) == 1: print(s)
# elif len(s) % 2 == 0: print(s[-len(s) // 2:] + s[:len(s) // 2])
# else: print(s[-len(s) // 2 + 1:] + s[:len(s) // 2 + 1])

# print(len(s) // 2 + len(s) % 2)

print(s[len(s)//2 + len(s) % 2:] + s[:len(s)//2 + len(s) % 2])