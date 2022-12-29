nums = [*map(int, input().split())]

print(max([_ for _ in nums if _ == nums.count(_)]) if [_ for _ in nums if _ == nums.count(_)] != [] else -1)
