city1, city2, city3 = input(), input(), input()

print(sorted([city1, city2, city3], key=len)[0], sorted([city1, city2, city3], key=len)[2], sep='\n')