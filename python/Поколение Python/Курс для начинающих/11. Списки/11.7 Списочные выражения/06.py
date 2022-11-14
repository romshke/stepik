palindromes = [_ for _ in range(100, 1000) if str(_) == str(_)[::-1]]

print(palindromes)