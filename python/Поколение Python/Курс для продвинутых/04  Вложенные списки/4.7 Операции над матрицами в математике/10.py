def matrix_multiplication(A, B, n, m, k):
    C = [[0 for _ in range(n)] for _ in range(k)]   
    for i in range(n):
        for j in range(k):
            for l in range(m):
                C[i][j] += A[i][l] * B[l][j]
                
    return C

n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]
input()
m, k = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    print(*matrix_multiplication(A, B, n, m, k)[i])