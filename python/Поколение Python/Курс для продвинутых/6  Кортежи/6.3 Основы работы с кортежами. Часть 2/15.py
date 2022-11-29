# def tribonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n == 3:
#         return 1
#     else:
#         return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# n = int(input())

# print(*(tribonacci(_) for _ in range(1, n + 1)))

n = int(input())
t1, t2, t3 = 1, 1, 1
for i in range(n):
    print(t1, end = ' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3