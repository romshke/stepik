def matrix_multiplication(A, B, n):
    C = [[0 for _ in range(n)] for _ in range(n)]   
    for i in range(n):
        for j in range(n):
            for l in range(n):
                C[i][j] += A[i][l] * B[l][j]
                
    return C

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

C = A.copy()

for _ in range(m - 1):
    C = matrix_multiplication(C, A, n)
    
for _ in range(n):
    print(*C[_])