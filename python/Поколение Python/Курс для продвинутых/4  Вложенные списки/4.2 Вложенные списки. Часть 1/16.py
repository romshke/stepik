list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

print(
    sum(j for i in list1 for j in i) / sum(len(i) for i in list1)
)