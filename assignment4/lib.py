## Custom library for importing some functions

# Partial pivoting
def partial_pivot(a,b,n):
    for i in range(n-1):
        if abs(a[i][i]) == 0:
            for j in range(i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[j], a[i] = a[i], a[j]  # interchange ith and jth rows of matrix 'a'
                    b[j], b[i] = b[i], b[j]  # interchange ith and jth elements of vector 'b'
    return a, b

def read_matrix(file):
    with open(file, 'r') as f:
        a = [[int(num) for num in line.split(' ')] for line in f]

    return a

# Function that returns the product of matrices a, b with n being the dimension of matrices (square)
def matrix_multiplication(a, b, n):
    c = [[ 0 for i in range(4) ] for j in range(4)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c

# Prints matrix as written in paper
def mat_print(a):
    for i in range(4):
        print(a[i])

# Forward-backward substitution
