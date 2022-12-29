nums = [_ for _ in range(1, int(input()) + 1)]
flag = True

while len(nums) > 1:
    if flag:
        nums = [nums[_] for _ in range(1, len(nums), 2)]
        # print(nums)
        flag = False
    else:
        nums = [nums[_] for _ in range(-2, -len(nums) - 1, -2)][::-1]
        # print(nums)
        flag = True

print(*nums)