with open('a3.txt', 'r') as f:
    a = [[int(num) for num in line.split(' ')] for line in f]

# holds a copy of matrix 'a' since it gets modified in the subsequent lines
with open('a3.txt', 'r') as f:
    A = [[int(num) for num in line.split(' ')] for line in f]

b = [[1,0,0], [0,1,0], [0,0,1]]   # will later on hold the inverse of matrix 'a'

# Dimensions of the matrix
n = 3

## Partial pivoting
def partial_pivot():
    for l in range(n-1):
        if abs(a[l][l]) == 0:
            for l1 in range(l+1,n):
                if abs(a[l1][l]) > abs(a[l][l]):
                    a[l1], a[l] = a[l], a[l1]  # interchange a[l] and a[l1]
                    b[l1], b[l] = b[l], b[l1]  # interchange b[l] and b[l1]

## Gauss-Jordan algorithm
def gauss_jordan():
    for i in range(n):
        partial_pivot()
        pivot = a[i][i]
        for l in range(n):
            b[i][l] = b[i][l]/pivot
        for r in range(i, n):
            a[i][r] = a[i][r]/pivot

        for k in range(n):
            if k != i and a[k][i] != 0:  # not clear from following line
                factor = a[k][i]
                for p in range(i, n):
                    b[k][p] = b[k][p] - factor*b[i][p]
                for j in range(i, n):
                    a[k][j] = a[k][j] - factor*a[i][j]

gauss_jordan()
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
c = matrix_multi(A,b)

# Prints array 'c' in matrix form
for j in range(n):
    print(c[j])
