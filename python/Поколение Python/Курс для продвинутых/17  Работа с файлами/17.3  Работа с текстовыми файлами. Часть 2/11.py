from functools import reduce

with open('nums.txt') as file:
    print(
        sum(
            reduce(
                lambda _1, _2: _1 + _2,
                [list(map(int, ''.join(map(lambda _: _ if _.isdigit() else ' ', line)).strip().split())) for line in file],
                []
            )
        )
    )