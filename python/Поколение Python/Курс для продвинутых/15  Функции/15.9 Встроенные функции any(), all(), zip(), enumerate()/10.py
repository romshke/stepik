abscissas, ordinates, applicates = (map(float, input().split()) for _ in range(3))
R = 2


print(all(map(lambda abcissa, ordinate, applicate: abcissa**2 + ordinate**2 + applicate**2 <= R**2, abscissas, ordinates, applicates)))


print(all(abcissa**2 + ordinate**2 + applicate**2 <= R**2 for abcissa, ordinate, applicate in zip(abscissas, ordinates, applicates)))