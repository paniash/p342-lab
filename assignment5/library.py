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

############################
# ASSIGNMENT-5 Functions
############################

def log_term(x, i):
    term = ((-1)**(i+1))*(((x-1)**i)/i)
    return term

# Logarithmic function expanded using Taylor expansion
def log(x, tol):
    summation = 0
    i = 1
    diff = log_term(x, i)
    while abs(diff) > tol:
        summation += diff
        i += 1
        diff = log_term(x, i)

    return summation

# Returns factorial of a non-negative integer
def factorial(x):
    prod = 1
    if x == 0:
        return 1
    else:
        for i in range(2,x+1):
            prod *= i
        return prod

# Returns terms of Taylor expansion of sine
def sine_term(x, i):
    term = (((-1)**i)/(factorial(2*i + 1)))*x**(2*i + 1)
    return term

# Sine function using Taylor expansion
def sin(x, tol):
    summation = 0
    i = 0
    diff = sine_term(x, i)
    while abs(diff) > tol:
        summation += diff
        i += 1
        diff = sine_term(x, i)

    return summation

def cos_term(x, i):
    term = (((-1)**i)/factorial(2*i))*x**(2*i)
    return term

# Cosine function using Taylor expansion
def cos(x, tol):
    summation = 0
    i = 0
    diff = cos_term(x, i)
    while abs(diff) > tol:
        summation += diff
        i += 1
        diff = cos_term(x, i)

    return summation

# Checks if the guess roots bracket around the actual root
def bracket(f, a, b):
    ct = 0   # keeps track of number of iterations
    beta = 1.5 # step value
    if a > b:
        print("'a' should be less than 'b'!!!")
        exit()
    else:
        prod = f(a)*f(b)
        if prod < 0:
            return a, b
        else:
            while prod > 0:
                if abs(f(a)) < abs(f(b)):
                    a = a - beta*(b-a)
                    ct += 1
                    prod = f(a) * f(b)

                elif abs(f(a)) > abs(f(b)):
                    b = b + beta*(b-a)
                    ct += 1
                    prod = f(a) * f(b)

            if ct > 12:
                print("Try another range.")
                exit()

            return a, b

# Bisection method of finding roots
def bisection(f, a, b, tol):
    a, b = bracket(f, a, b)
    ct = 0  # keeps track of number of iterations
    iterations = []
    root_i = []
    abs_error = [0]
    max_iter = 200
    while (abs(a - b) >= tol):
        c = (a + b)/2
        prod = f(a) * f(c)
        if prod < 0:
            b = c
        elif prod > 0:
            a = c

        iterations.append(ct)
        ct += 1
        root_i.append(c)
        if ct > 0:
            error = abs(root_i[ct] - root_i[ct-1])
        abs_error.append(error)


        if (ct >= 200):
            print("Too many iterations!!!")
            exit()

    for i in range(ct):
        print("Absolute error: {}  Iterations: {}".format(abs_error[i], iterations[i]))

    return c

# # Regular Falsi method of finding roots
# def regular_falsi(f, a, b, tol):
#     a, b = bracket(f, a, b)
#     ct = 0  # keeps track of number of iterations
#     while True:
#         c = b - (((b-a)*f(b))/(f(b) - f(a)))
#         prod = f(a) * f(c)
#         if prod < 0:
#             b = c
#         else:
#             a = c

#         ct += 1
#         if (f(c) < tol):
#             break

#     return c
