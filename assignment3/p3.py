# Find the inverse of the matrix (FYI inverse exists) and check A A-1 = I :
#           1   -3    7
#     A =  -1    4   -7
#          -1    3   -6
# You should write separate functions for --
# (a) partial pivoting, (b) Gauss-Jordan method, (c) matrix multiplication
# then call them from the main function.Read the matrices from files. Avoid using “break” but may
# use “next” or “continue”

# Read matrix 'A' from file a3.txt
with open('a3.txt', 'r') as f:
    A = [[int(num) for num in line.split(' ')] for line in f]

# holds a copy of matrix 'A' since it gets modified in the subsequent lines
with open('a3.txt', 'r') as f:
    A0 = [[int(num) for num in line.split(' ')] for line in f]

b = [[1,0,0], [0,1,0], [0,0,1]]   # will later on hold the inverse of matrix 'A'

# Dimension of the matrix
n = 3

## Partial pivoting on matrix 'a' and vector 'b'
def partial_pivot(a,b):
    for i in range(n-1):
        if abs(a[i][i]) == 0:
            for j in range(i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[j], a[i] = a[i], a[j]  # interchange ith row and jth row of matrix 'a'
                    b[j], b[i] = b[i], b[j]  # interchange ith row and jth row of vector 'b'

## Gauss-Jordan algorithm
def gauss_jordan(a,b):
    partial_pivot(a,b)
    for i in range(n):
        pivot = a[i][i]
        for l in range(n):
            if b[i][l] != 0:
                b[i][l] = b[i][l]/pivot
        for c in range(i, n):
            a[i][c] = a[i][c]/pivot

        for k in range(n):
            if k != i and a[k][i] != 0:  # not clear from following line
                factor = a[k][i]
                for j in range(i, n):
                    a[k][j] = a[k][j] - factor*a[i][j]
                for p in range(n):
                    if b[i][p] != 0:
                        b[k][p] = b[k][p] - factor*b[i][p]

gauss_jordan(A,b)
print("Inverse:")

# Prints inverse in a matrix form
for i in range(n):
    print(b[i])

## Verifying that AA^{-1} = I
# Function to multiply 2 matrices, mat1 and mat2
def matrix_multi(mat1, mat2, n=3):   # The function assumes multiplication of square matrices
    prod = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                prod[i][j] += mat1[i][k]*mat2[k][j]

    return prod

print("\nVerification of inverse:")
c = matrix_multi(A0,b)

# Prints array 'c' in matrix form
for j in range(n):
    print(c[j])

## OUTPUT:
# Inverse:
# [-3.0, 3.0, -7.0]
# [1.0, 1.0, 0]
# [1.0, 0, 1.0]

# Verification of inverse:
# [1.0, 0.0, 0.0]
# [0.0, 1.0, 0.0]
# [0.0, 0.0, 1.0]
