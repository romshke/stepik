for bulls in range(1, 100 // 10 + 1):
    for cows in range(1, 100 // 5 + 1):
        for calves in range(1, 1000 // 5 + 1):
            if bulls * 10 + cows * 5 + calves * 0.5 == 100 and bulls + cows + calves == 100: print(bulls, cows, calves)