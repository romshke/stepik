l1, l2 = input().split(), input().split()
print(*(int(l1[i]) + int(l2[i]) for i in range(len(l1))))