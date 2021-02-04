#  _     _ _
# | |   (_) |__  _ __ __ _ _ __ _   _
# | |   | | '_ \| '__/ _` | '__| | | |
# | |___| | |_) | | | (_| | |  | |_| |
# |_____|_|_.__/|_|  \__,_|_|   \__, |
#                               |___/

# Imports
import random

# Partial pivoting with matrix 'a', vector 'b', and dimension 'n'
def partial_pivot(a, b, n):
    count = 0   # keeps a track of number of exchanges (odd number of exchanges adds a phase of -1 to determinant)
    for i in range(n-1):
        if abs(a[i][i]) == 0:
            for j in range(i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[j], a[i] = a[i], a[j]  # interchange ith and jth rows of matrix 'a'
                    count += 1
                    b[j], b[i] = b[i], b[j]  # interchange ith and jth elements of vector 'b'

    return a, b, count

# Read matrix from a file given as a string (space separated file)
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
    U = [[0 for i in range(len(a))] for j in range(len(a))]
    L = [[0 for i in range(len(a))] for j in range(len(a))]

    for i in range(len(a)):
        L[i][i] = 1

    for j in range(len(a)):
        for i in range(len(a)):
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
    y = [0 for i in range(len(b))]

    for i in range(len(b)):
        total = 0
        for j in range(i):
            total += L[i][j] * y[j]
        y[i] = b[i] - total

    x = [0 for i in range(len(b))]

    for i in reversed(range(len(b))):
        total = 0
        for j in range(i+1, len(b)):
            total += U[i][j] * x[j]
        x[i] = (y[i] - total)/U[i][i]

    return x

# Solves for the set of linear equations Ax = b, using LU decomposition
def lin_solver(A, b):
    partial_pivot(A, b, len(A))
    U, L = crout(A)
    x = forward_backward(U, L, b)
    return x

# Returns the determinant of matrix 'a'
def determinant(a):
    b = [0 for i in range(len(a))]
    a, b, count = partial_pivot(a, b, len(a))
    U = crout(a)[0]
    det = 1
    for i in range(len(a)):
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

# Checks if the guess roots bracket around the actual root and if not, then
# accordingly evaluates supposed roots
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
def write_table(file, col1, col2, col3):
    table = [[ 0 for i in range(3)] for j in range(len(col1))]
    f = open(file, 'w')
    for i in range(len(col1)):
        for j in range(3):
            table[i][:] = [col1[i], col2[i], col3[i]]

        f.writelines(str(table[i])[1:-1] + "\n")
    f.close()

    return table

# Outputs the data into a pretty table format
def print_table(table, head1, head2, head3):
    data = table.copy()
    col1 = [head1]       # stores first column
    col2 = [head2]   # stores second column
    col3 = [head3]      # stores third column
    for i in range(len(data)):
        col1.append(data[i][0])
        col2.append(data[i][1])
        col3.append(data[i][2])

    for i in range(len(data)+1):
        print(col1[i], col2[i], col3[i])

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
    # lims is a list item containing 2 limits, [lower_limit, upper_limit]
    if(len(lims) != 2):
        print("Please enter 2 limits only")
        exit()

    tol = (lims[1] - lims[0])/N
    total = func(lims[0]) + func(lims[1])

    for i in range(1, N):
        if i % 2 != 0:
            coeff = 4
        else:
            coeff = 2

        total += coeff * func(lims[0] + i*tol)

    total = total * tol/3

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

##############################################################
#### Functions to be imported for differential equations #####
##############################################################

# Solves differential equation using forward Euler
def forward_euler(dydx, y0, x0, xf, step_size):
    """ Yields solution from x=x0 to x=xf """
    x = []
    y = []
    x.append(x0)
    y.append(y0)

    n = int((xf-x0)/step_size)      # no. of steps
    for i in range(n):
        x.append(x[i] + step_size)

    for i in range(n):
        y.append(y[i] + step_size * dydx(y[i], x[i]))

    return x, y

# Solves differential equation using Runge-Kutta method
def runge_kutta(d2ydx2, dydx, x0, y0, z0, xf, step_size):
    """ Yields solution from x=x0 to x=xf
    y(x0) = y0 & y'(x0) = z0
    z = dy/dx
    """
    x = []
    y = []
    z = []      # dy/dx
    x.append(x0)
    y.append(y0)
    z.append(z0)

    n = int((xf-x0)/step_size)      # no. of steps
    for i in range(n):
        x.append(x[i] + step_size)
        k1 = step_size * dydx(x[i], y[i], z[i])
        l1 = step_size * d2ydx2(x[i], y[i], z[i])
        k2 = step_size * dydx(x[i] + step_size/2, y[i] + k1/2, z[i] + l1/2)
        l2 = step_size * d2ydx2(x[i] + step_size/2, y[i] + k1/2, z[i] + l1/2)
        k3 = step_size * dydx(x[i] + step_size/2, y[i] + k2/2, z[i] + l2/2)
        l3 = step_size * d2ydx2(x[i] + step_size/2, y[i] + k2/2, z[i] + l2/2)
        k4 = step_size * dydx(x[i] + step_size, y[i] + k3, z[i] + l3)
        l4 = step_size * d2ydx2(x[i] + step_size, y[i] + k3, z[i] + l3)

        y.append(y[i] + (k1 + 2*k2 + 2*k3 + k4)/6)
        z.append(z[i] + (l1 + 2*l2 + 2*l3 + l4)/6)

    return x, y, z


# Returns the result of Lagrange's interpolation formula
def lagrange_interpolation(zeta_h, zeta_l, yh, yl, y):
    zeta = zeta_l + (zeta_h - zeta_l) * (y - yl)/(yh - yl)
    return zeta


# Solves 2nd order ODE given Dirichlet boundary conditions
def shooting_method(d2ydx2, dydx, x0, y0, xf, yf, z_guess1, z_guess2, step_size, tol=1e-6):
    '''x0: Lower boundary value of x
    y0 = y(x0)
    xf: Upper boundary value of x
    yf = y(xf)
    z = dy/dx
    '''
    x, y, z = runge_kutta(d2ydx2, dydx, x0, y0, z_guess1, xf, step_size)
    yn = y[-1]

    if abs(yn - yf) > tol:
        if yn < yf:
            zeta_l = z_guess1
            yl = yn

            x, y, z = runge_kutta(d2ydx2, dydx, x0, y0, z_guess2, xf, step_size)
            yn = y[-1]

            if yn > yf:
                zeta_h = z_guess2
                yh = yn

                # calculate zeta using Lagrange interpolation
                zeta = lagrange_interpolation(zeta_h, zeta_l, yh, yl, yf)

                # using this zeta to solve using RK4
                x, y, z = runge_kutta(d2ydx2, dydx, x0, y0, zeta, xf, step_size)
                return x, y, z

            else:
                print("Bracketing FAIL! Try another set of guesses.")


        elif yn > yf:
            zeta_h = z_guess1
            yh = yn

            x, y, z = runge_kutta(d2ydx2, dydx, x0, y0, z_guess2, xf, step_size)
            yn = y[-1]

            if yn < yf:
                zeta_l = z_guess2
                yl = yn

                # calculate zeta using Lagrange interpolation
                zeta = lagrange_interpolation(zeta_h, zeta_l, yh, yl, yf)

                x, y, z = runge_kutta(d2ydx2, dydx, x0, y0, zeta, xf, step_size)
                return x, y, z

            else:
                print("Bracketing FAIL! Try another set of guesses.")


    else:
        return x, y, z         # bang-on solution with z_guess1


######################################################################
###################### CURVE FIT #####################################
######################################################################

# Function to read x and y data values from a CSV file
def read_data(file):
    x = []   # holds x vals
    y = []   # holds y vals
    ct = 0   # variable to check if value is in first column (x) or 2nd column (y)
    with open(file, 'r') as f:
        for line in f:
            for num in line.split(','):
                if ct % 2 == 0:
                    x.append(float(num))
                else:
                    y.append(float(num))

                ct += 1

    return x, y

# # Returns the intercept and slope for a linear fit, given a set of data points
# def linear_fit(xvals, yvals):
#     '''xvals, yvals: data points given as a list (separately) as input
#     Return values:
#         a: intercept
#         b: slope
#         Linear plot: y = a + b*x
#     '''
#     n = len(xvals)   # number of datapoints
#     xbar = sum(xvals)/n  # average value of all datapoints represented along x
#     ybar = sum(yvals)/n  # average value of all datapoints represented along y

#     sxx = 0  # sigma**2 * n
#     for i in xvals:
#         sxx += i**2 - xbar**2

#     sxy = 0  # covariance * n
#     for i in range(len(xvals)):
#         sxy += x[i] * y[i] - xbar * ybar

#     # Evaluate slope and intercept
#     b = sxy/sxx
#     a = ybar - b*xbar

#     return b, a

# Returns the intercept and slope for a linear fit, given a set of data points
def linear_fit(xvals, yvals):
    '''xvals, yvals: data points given as a list (separately) as input
    Return values:
        a0: intercept
        a1: slope
        Linear plot: y = a0 + a1*x
    '''
    n = len(xvals)   # number of datapoints

    sx = sum(xvals)
    sy = sum(yvals)
    sx2 = 0
    sxy = 0
    for i in range(n):
        sx2 += xvals[i]**2
        sxy += xvals[i] * yvals[i]

    # Construct appropriate matrices to form linear equations, Ax = b
    A = [[n, sx], [sx, sx2]]
    b = [sy, sxy]

    sol = lin_solver(A, b)

    return sol

# Quadratic fit using least square method
def quad_fit(xvals, yvals):
    '''xvals, yvals: data points given as a list (separately) as input
    Return values:
        a0, a1, a2
        Quadratic plot: y = a0 + a1*x + a2*x**2
    '''
    n = len(xvals)

    sx1 = sum(xvals)
    sx2 = 0
    sx3 = 0
    sx4 = 0

    sy = sum(yvals)
    sxy = 0
    sx2y = 0

    for i in range(n):
        sx2 += xvals[i]**2
        sx3 += xvals[i]**3
        sx4 += xvals[i]**4
        sxy += xvals[i] * yvals[i]
        sx2y += xvals[i]**2 * yvals[i]

    # Construct matrices from the above calculated values
    A = [[n, sx1, sx2], [sx1, sx2, sx3], [sx2, sx3, sx4]]
    b = [sy, sxy, sx2y]

    # Solve for coefficients a0, a1, a2 for, y = a0 + a1*x + a2*x**2
    sol = lin_solver(A, b)

    return sol


# Evaluates pearson's r for a given curve fit
def pearson_r(xvals, yvals):
    '''xvals, yvals: data points given as a list (separately) as input
    '''
    n = len(xvals)   # number of datapoints

    xbar = sum(xvals)/n
    ybar = sum(yvals)/n

    sxx = 0  # sigma**2 * n
    for i in xvals:
        sxx += (i - xbar)**2

    sxy = 0  # covariance * n
    for i in range(n):
        sxy += (xvals[i] - xbar) * (yvals[i] - ybar)

    syy = 0
    for j in yvals:
        syy += (j - ybar)**2

    r2 = sxy**2 / (sxx * syy)
    r = r2**(0.5)

    return r
