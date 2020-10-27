## Custom library for importing helper functions
import random

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

## Logarithmic function expanded using Taylor expansion
# ln (x) = limit n -> \infty {n * (x**(1/n) - 1)}
def log(x, tol=1e-6):
    n = 10000
    return n * (x**(1/n) - 1)

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
def sin(x, tol=1e-6):
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
def cos(x, tol=1e-6):
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
    iterations = []
    root_i = []
    abs_error = []
    max_iter = 200   # maximum iterations allowed
    for i in range(max_iter):
        c = (a+b)/2
        prod = f(a) * f(c)
        if prod < 0:
            b = c
        elif prod > 0:
            a = c

        iterations.append(i)
        root_i.append(c)
        error = abs(root_i[i] - root_i[i-1])
        abs_error.append(error)

        if abs(a-b)<tol:
            return c, abs_error, iterations

# Regula Falsi method of finding roots
def regula_falsi(f, a, b, tol):
    a, b = bracket(f, a, b)
    iterations = []
    root_i = []
    abs_error = []
    max_iter = 200
    c = a  # initial guess for the root
    for i in range(max_iter):
        c_prev = c
        c = b - ((b-a)*f(b))/(f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        elif f(a) * f(c) > 0:
            a = c

        iterations.append(i)
        root_i.append(c)
        error = abs(root_i[i] - root_i[i-1])
        abs_error.append(error)

        if abs(c - c_prev) < tol:
            return c, abs_error, iterations


# Derivation function at x = x0 with default tolerance (h-value) = 1e-6
def derivative(f, x0, tol=1e-6):
    df = (f(x0+tol) - f(x0-tol))/(2*tol)
    return df

# Double derivative of a function with default tolerance (h-value) = 1e-6
def double_derivative(f, x0, tol=1e-6):
    f1 = derivative(f, x0) + tol
    f0 = derivative(f, x0) - tol
    ddf = (f1-f0)/(2*tol)
    return ddf

# Newton-Raphson method of finding roots
def newton_raphson(f, x0, tol):
    iterations = []
    abs_error = []
    max_iter = 200
    for i in range(max_iter):
        x_prev = x0
        x0 = x0 - (f(x0)/derivative(f, x0))
        iterations.append(i)
        abs_error.append(abs(x0 - x_prev))

        if abs(x0 - x_prev)<tol:
            return x0, abs_error, iterations

# Writes the data of bisection, regula-falsi, and newton-raphson into external csv files
def write_table(file, iterations, abs_error):
    table = [[ 0 for i in range(2)] for j in range(len(iterations) - 1)]
    f = open(file, 'w')
    for i in range(len(iterations) - 1):
        for j in range(2):
            table[i][:] = [iterations[i], abs_error[i]]

        f.writelines(str(table[i])[1:-1] + "\n")
    f.close()

    return table

# Outputs the data into a pretty table format
def print_table(table):
    data = table.copy()
    col1 = ["Iterations"]       # stores first column
    col2 = ["Absolute error"]   # stores second column
    for i in range(len(data)):
        col1.append(data[i][0])
        col2.append(data[i][1])

    for i in range(len(data)):
        print(col1[i], col2[i])

    return 0

# Polynomial function definition
# The coefficients is passed in the form of a list as the argument
def polynomial(coeffs, x):
    degree = len(coeffs) - 1

    func = 0   # polynomial function
    for i in range(len(coeffs)):
        func += coeffs[i] * x**(degree-i)

    return func

## Deflation function that returns the coefficients of the deflated function (x0 is one of the roots)
# Uses synthetic division
def deflation(coeffs, x0):
    new_coeffs = []
    new_coeffs.append(coeffs[0])
    for i in range(1, len(coeffs)):
        new_coeffs.append(x0*new_coeffs[i-1] + coeffs[i])

    new_coeffs.pop()    # removes the last '0' from the new set of coefficients

    return new_coeffs

def poly_derivative(coeffs, alpha, tol=1e-6):
    dv = (polynomial(coeffs, alpha+tol) - polynomial(coeffs, alpha-tol))/(2*tol)
    return dv

def poly_double_derivative(coeffs, alpha, tol=1e-6):
    ddv = (poly_derivative(coeffs, alpha+tol) - poly_derivative(coeffs, alpha-tol))/(2*tol)
    return ddv

# Computes variables in Laguerre's method
def laguerre(coeffs, alpha, tol):
    n = len(coeffs) - 1    # n is the degree of the polynomial
    max_iter = 200

    if abs(polynomial(coeffs, alpha)) < tol:
        return alpha

    else:
        for i in range(max_iter):
            G = poly_derivative(coeffs, alpha)/(polynomial(coeffs, alpha))
            H = G**2 - (poly_double_derivative(coeffs, alpha)/polynomial(coeffs, alpha))

            denom1 = (G + ((n-1)*(n*H - G**2))**0.5)
            denom2 = (G - ((n-1)*(n*H - G**2))**0.5)
            if denom1 > denom2:
                a = n/denom1

            else:
                a = n/denom2

            alpha_prev = alpha
            alpha = alpha - a

            if abs(alpha - alpha_prev) < tol:
                x0 = alpha
                return x0

# Polynomial root solver using Laguerre's method
def polynomial_solver(coeffs, alpha, tol=1e-6):
    roots = []
    index = -1  # holds index position of newly added root
    while(len(coeffs) > 1):
        roots.append(laguerre(coeffs, alpha, tol))
        index += 1
        coeffs = deflation(coeffs, roots[index])

    return roots

##################################################
############### Assignment 6 #####################
##################################################

# Integration using midpoint method
def integrate_midpoint(func, lims, N):
    # lims must only contain 2 limits
    if(len(lims) != 2):
        print("Please enter 2 limits only!")
        exit()

    N = 100
    tol = (lims[1] - lims[0])/N
    total = 0
    for i in range(1,N+1):
        x = ((i-1)*tol + i*tol + 2*lims[0])/2
        total += tol*func(x)

    return total


# Integration using trapezoidal rule
def integrate_trapezoid(func, lims, N):
    # lims must contain only 2 limits
    if(len(lims) != 2):
        print("Please enter 2 limits only")
        exit()

    tol = (lims[1] - lims[0])/N
    total = 0
    for i in range(1, N+1):
        x1 = lims[0] + i*tol
        x0 = x1 - tol
        term_i = (func(x0) + func(x1))*(tol/2)
        total += term_i

    return total

# Integration using Simpson rule
def integrate_simpson(func, lims, N):
    # lims is a list item containing 2 limits
    if(len(lims) != 2):
        print("Please enter 2 limits only")
        exit()

    tol = (lims[1] - lims[0])/N
    total = 0
    for i in range(1, N+1, 2):   # integrating from x0 -> x2; then x2 -> x4. Hence increment step size is 2
        x2 = lims[0] + i*tol
        x0 = x2 - tol
        x1 = (x0 + x2)/2
        term_i = (func(x0) + 4*func(x1) + func(x2))*(tol/3)
        total += term_i

    return total

# Function to calculate the ceil of a number
def ceil(x):
    return int(x) + 1

# Monte Carlo integration
def monte_carlo(func, lims, N):
    # Generate list of N random points between lims
    xrand = []
    for i in range(N):
        xrand.append(random.uniform(lims[0], lims[1]))

    summation = 0
    for i in range(N):
        summation += func(xrand[i])

    total = (lims[1]-lims[0])/float(N) * summation

    return total, xrand
