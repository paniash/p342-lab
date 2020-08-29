a = [[1,-3,7], [-1,4,-7], [-1,3,-6]]
b = [[1,0,0], [0,1,0], [0,0,1]]
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
        b[i] = b[i]/pivot
        for r in range(i, n):
            a[i][r] = a[i][r]/pivot

        for k in range(n):
            if k != i and a[k][i] != 0:  # not clear from following line
                factor = a[k][i]
                b[k] = b[k] - a[k][i]*b[i]
                for j in range(i, n):
                    a[k][j] = a[k][j] - factor*a[i][j]

gauss_jordan()
print(b)
