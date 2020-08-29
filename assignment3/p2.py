# Gauss-Jordan method of solving set of linear equations
# 2y + 5z = 1
# 3x - y + 2z = -2
# x - y + 3z = 3

## Define the problem as Ax = b where x = [x1, x2, x3]
# Read matrix 'A' from file a2.txt
with open('a2.txt', 'r') as f:
    A = [[int(num) for num in line.split(' ')] for line in f]

# Vector b
b = [1, -2, 3]

# Number of linear equations
n = 3

## Partial pivoting
def partial_pivot(a,b):
    for i in range(n-1):
        if abs(a[i][i]) == 0:
            for j in range(i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[j], a[i] = a[i], a[j]  # interchange a[i] and a[j]
                    b[j], b[i] = b[i], b[j]  # interchange b[i] and b[j]


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
print(b)
