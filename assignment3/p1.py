# Gauss-Jordan method of solving set of linear equations
# x + 3y + 2z = 2
# 2x + 7y + 7z = -1
# 2x + 5y + 2z = 7

## Define the problem as AX = b where X = [x, y, z]
# Read matrix 'A' from file a1.txt
with open('a1.txt', 'r') as f:
    A = [[int(num) for num in line.split(' ')] for line in f]

# Vector b
b = [2, -1, 7]

# Number of linear equations
n = 3

## Partial pivoting
def partial_pivot(a,b):
    for i in range(n-1):
        if abs(a[i][i]) == 0:
            for j in range(i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[j], a[i] = a[i], a[j]  # interchange ith and jth rows of matrix 'a'
                    b[j], b[i] = b[i], b[j]  # interchange ith and jth elements of vector 'b'


## Gauss-Jordan algorithm
def gauss_jordan(a,b):
    partial_pivot(a,b)
    for i in range(n):
        pivot = a[i][i]
        b[i] = b[i]/pivot
        for c in range(i, n):
            a[i][c] = a[i][c]/pivot

        for k in range(n):
            if k != i and a[k][i] != 0:
                factor = a[k][i]
                b[k] = b[k] - factor*b[i]
                for j in range(i, n):
                    a[k][j] = a[k][j] - factor*a[i][j]

gauss_jordan(A,b)
print("Solution:")
print("x =", b[0], ", y =", b[1], ", z =", b[2])

## OUTPUT:
# Solution:
# x = 3.0 , y = 1.0 , z = -2.0
