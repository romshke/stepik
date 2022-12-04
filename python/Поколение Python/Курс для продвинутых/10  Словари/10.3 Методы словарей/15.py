words = list(map(lambda _: _.strip('.,!?:;-'), input().lower().split()))

words_dict = {_: words.count(_) for _ in set(words)}

print(sorted(words_dict.items(), key = lambda _: (_[1], _[0]))[0][0])