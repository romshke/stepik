n, m, k = int(input()), int(input()), int(input())
print('YES' if ((k >= n and k % n == 0) or (k >= m and k % m == 0)) and n * m > k else 'NO')