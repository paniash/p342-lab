# Gauss-Jordan method of solving set of linear equations
# x + 3y + 2z = 2
# 2x + 7y +7z = -1
# 2x + 5y + 2z = 7

## Define the problem as aX = b where X = [x1, x2, x3]
# Read matrix 'a' from file a1.txt
with open('a1.txt', 'r') as f:
    a = [[int(num) for num in line.split(' ')] for line in f]

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
                    a[j], a[i] = a[i], a[j]  # interchange a[i] and a[j]
                    b[j], b[i] = b[i], b[j]  # interchange b[i] and b[j]


## Gauss-Jordan algorithm
def gauss_jordan(a,b):
    for i in range(n):
        partial_pivot(a,b)
        pivot = a[i][i]
        b[i] = b[i]/pivot
        for r in range(i, n):
            a[i][r] = a[i][r]/pivot

        for k in range(n):
            if k != i and a[k][i] != 0:  # not clear from following line
                factor = a[k][i]
                b[k] = b[k] - a[k][i]*b[i]
                for j in range(i, n):
                    a[k][j] = a[k][j] - factor*a[i][j]

gauss_jordan(a,b)
print(b)
