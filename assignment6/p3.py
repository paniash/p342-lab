# Numerically integrate exp^{-x^2} using midpoint, trapezoidal and simpson methods with a maximum error of 0.00
from library import integrate_midpoint, integrate_trapezoid, integrate_simpson, ceil

# Define e
exp = 2.7183

# Defining the integrand
def f(x):
    return exp**(-x**2)

# Calculates N for a given upper bound for all functions
def error_n_midpoint(func, lims):
    n = (((lims[1] - lims[0])**3/(24*0.001))*abs(func(0)))**0.5
    return ceil(n)

def error_n_trapezoid(func, lims):
    n = (((lims[1] - lims[0])**3/(12*0.001))*abs(func(0)))**0.5
    return ceil(n)

def error_n_simpson(func, lims):
    n = (((lims[1] - lims[0])**5/(180*0.001))*abs(func(0)))**0.25
    if (ceil(n) % 2 != 0):
        return ceil(n) + 1
    else:
        return ceil(n)

# Second derivative of exp(-x**2)
def double_derivative(x):
    return (4*x**2 - 2)*exp**(-x**2)

# Fourth derivative of exp(-x**2)
def quad_derivative(x):
    return (16*x**4 - 48*x**2 + 12)*exp**(-x**2)

# Evaluating values of N for the error upper bound
n_mid = error_n_midpoint(double_derivative, [0,1])
n_trap = error_n_trapezoid(double_derivative, [0,1])
n_simp = error_n_simpson(quad_derivative, [0,1])

# Evaluating the integral
sol1 = integrate_midpoint(f, [0,1], n_mid)
sol2 = integrate_trapezoid(f, [0,1], n_trap)
sol3 = integrate_simpson(f, [0,1], n_simp)

print("Integral through various methods:\n")
print("Midpoint: ", sol1, "\nTrapezoid: ", sol2, "\nSimpson: ", sol3)


##################################################
################ OUTPUT #########################
##################################################

# Integral through various methods:

# Midpoint:  0.7471296111426919
# Trapezoid:  0.7464599944330834
# Simpson:  0.827708873985558
