words = input().split()

words_dict = {index: [item, words[:index + 1].count(item)] for index, item in enumerate(words)}

print(*(_[1] for _ in words_dict.values()))