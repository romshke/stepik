def matrix_multiplication(A, B):
    C = [[0 for i in range(2)] for i in range(2)]   
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
                
    return C

a = [[1, 0],
     [4, 1]]

result = a.copy()
    
for _ in range(24):
    result = matrix_multiplication(result, a)
    
for i in range(2):
    for j in range(2):
        print(str(result[i][j]).ljust(5), end='')
    print()

# 1 0   1 0   1 0
# 4 1   4 1   8 1