# Gauss-Jordan method of solving set of linear equations
# x + 3y + 2z = 2
# 2x + 7y +7z = -1
# 2x + 5y + 2z = 7

## Define the problem as aX = b where X = [x1, x2, x3]
# Define a
a = [[0, 2, 5], [3, -1, 2], [1, -1, 3]]

# Define b
b = [1, -2, 3]

# Number of linear equations
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
for i in range(n):
    partial_pivot()
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

print(b)
