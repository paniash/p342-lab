# Numerically integrate x/(1+x) from 1 to 3 using methods: midpoint, trapezoid, simpson for respective values of N => 5, 10, 25

from library import integrate_midpoint, integrate_trapezoid, integrate_simpson, write_table, print_table
import matplotlib.pyplot as plt

def f(x):
    return x/(1+x)

N = [6, 10, 26]
analytic_sol = 1.3068

# Midpoint method
sol1_list = []  # Holds integral value for N values = 5,10,25
abs1_error = []  # the absolute difference between analytic solution and numerical solution
for i in N:
    sol1 = integrate_midpoint(f, [1,3], i)
    sol1_list.append(sol1)
    abs1_error.append(abs(analytic_sol - sol1))
table1 = write_table('table_midpoint.csv', N, sol1_list, abs1_error)
print("\nMidpoint method:")
print_table(table1, "N", "Integral", "Absolute error")

# Trapezoid method
sol2_list = []
abs2_error = []
for i in N:
    sol2 = integrate_trapezoid(f, [1,3], i)
    sol2_list.append(sol2)
    abs2_error.append(abs(analytic_sol - sol2))
table2 = write_table('table_trapezoid.csv', N, sol2_list, abs2_error)
print("\nTrapezoid method:")
print_table(table2, "N", "Integral", "Absolute error")

# Simpson method
sol3_list = []
abs3_error = []
for i in N:
    sol3 = integrate_simpson(f, [1,3], i)
    sol3_list.append(sol3)
    abs3_error.append(abs(analytic_sol - sol3))
table3 = write_table('table_simpson.csv', N, sol3_list, abs3_error)
print("\nSimpson method:")
print_table(table3, "N", "Integral", "Absolute error")


##################################################
################ OUTPUT #########################
##################################################

# Midpoint method:
# N Integral Absolute error
# 6 1.3077156791250208 0.0009156791250208851
# 10 1.3071646395900398 0.00036463959003985025
# 26 1.3068990323038625 9.903230386254513e-05

# Trapezoid method:
# N Integral Absolute error
# 6 1.3051226551226551 0.001677344877344833
# 10 1.3062285968245722 0.0005714031754278093
# 26 1.3067603809022117 3.961909778826822e-05

# Simpson method:
# N Integral Absolute error
# 6 1.2655102522749582 0.04128974772504179
# 10 1.2819245627554052 0.024875437244594734
# 26 1.2972415707499416 0.009558429250058342
