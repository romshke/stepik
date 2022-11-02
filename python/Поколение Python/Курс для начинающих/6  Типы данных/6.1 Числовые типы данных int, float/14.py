n = input()

if int(sorted(list(n))[2]) - int(sorted(list(n))[0]) == int(sorted(list(n))[1]): print("Число интересное")
else: print("Число неинтересное")