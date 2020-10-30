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
print_table(table1, "\nN", "Integral", "Absolute error")

# Trapezoid method
sol2_list = []
abs2_error = []
for i in N:
    sol2 = integrate_trapezoid(f, [1,3], i)
    sol2_list.append(sol2)
    abs2_error.append(abs(analytic_sol - sol2))
table2 = write_table('table_trapezoid.csv', N, sol2_list, abs2_error)
print_table(table2, "\nN", "Integral", "Absolute error")

# Simpson method
sol3_list = []
abs3_error = []
for i in N:
    sol3 = integrate_simpson(f, [1,3], i)
    sol3_list.append(sol3)
    abs3_error.append(abs(analytic_sol - sol3))
table3 = write_table('table_simpson.csv', N, sol3_list, abs3_error)
print_table(table3, "\nN", "Integral", "Absolute error")
