## Custom library for importing helper functions

# Partial pivoting with matrix 'a', vector 'b', and dimension 'n'
def partial_pivot(a,b,n):
    count = 0   # keeps a track of number of exchanges (odd number of exchanges adds a phase of -1 to determinant)
    for i in range(n-1):
        if abs(a[i][i]) == 0:
            for j in range(i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[j], a[i] = a[i], a[j]  # interchange ith and jth rows of matrix 'a'
                    count += 1
                    b[j], b[i] = b[i], b[j]  # interchange ith and jth elements of vector 'b'

    return a, b, count

# Read matrix from a file given as a string
def read_matrix(file):
    with open(file, 'r') as f:
        a = [[int(num) for num in line.split(' ')] for line in f]

    return a

# Prints matrix as written on paper
def mat_print(a, n=4):
    for i in range(n):
        print(a[i])

# Crout's method of LU decomposition
def crout(a):
    U = [[0 for i in range(4)] for j in range(4)]
    L = [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        L[i][i] = 1

    for j in range(4):
        for i in range(4):
            total = 0
            for k in range(i):
                total += L[i][k] * U[k][j]

            if i == j:
                U[i][j] = a[i][j] - total

            elif i > j:
                L[i][j] = (a[i][j] - total)/U[j][j]

            else :
                U[i][j] = a[i][j] - total

    return U, L

# Forward-backward substitution function which returns the solution x = [x1, x2, x3, x4]
def forward_backward(U, L, b):
    y = [0 for i in range(4)]

    for i in range(4):
        total = 0
        for j in range(i):
            total += L[i][j] * y[j]
        y[i] = b[i] - total

    x = [0 for i in range(4)]

    for i in reversed(range(4)):
        total = 0
        for j in range(i+1, 4):
            total += U[i][j] * x[j]
        x[i] = (y[i] - total)/U[i][i]

    return x

# Solves for the set of linear equations Ax = b, using LU decomposition
def lin_solver(A, b):
    partial_pivot(A, b, 4)
    U, L = crout(A)
    x = forward_backward(U, L, b)
    return x

# Returns the determinant of matrix 'a'
def determinant(a):
    b = [0 for i in range(4)]
    a, b, count = partial_pivot(a, b, 4)
    U = crout(a)[0]
    det = 1
    for i in range(4):
       det *= U[i][i]

    # if even number of row exchanges, determinant remains the same, else is multiplied by -1
    if count % 2 == 0:
        return det
    else:
        return -det
