# Question 1b
from library import bisection, regula_falsi, newton_raphson, write_table, cos, print_table
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("PDF")  # renders the plots in pdf format

def f(x):
    return -(x+cos(x))

print("Roots in the following methods:\n")
root0, abs_error0, iterations0 = bisection(f, -2, 0, 1e-6)
abs_error0.remove(0)
iterations0.remove(0)
print("Bisection:", root0)

root1, abs_error1, iterations1 = regula_falsi(f, -2, 0, 1e-6)
abs_error1.remove(0)
iterations1.remove(0)
print("Regula-falsi:", root1)

root2, abs_error2, iterations2 = newton_raphson(f, -2, 1e-6)
print("Newton-Raphson:", root2)

table0 = write_table('bisection_b.csv', iterations0, abs_error0)
table1 = write_table('regula_falsi_b.csv', iterations1, abs_error1)
table2 = write_table('newton_raphson_b.csv', iterations2, abs_error2)

print("\nData file for various methods: \n")
print("Bisection: ")
print_table(table0)

print("\nRegula Falsi: ")
print_table(table1)

print("\nNewton-Raphson: ")
print_table(table2)

plt.plot(iterations0, abs_error0, label='Bisection')
plt.plot(iterations1, abs_error1, label='Regula Falsi')
plt.plot(iterations2, abs_error2, label='Newton Raphson')
plt.xlabel("Iterations")
plt.ylabel("Absolute error")
plt.legend()
plt.show()

plt.savefig("plot_1b.pdf")


##################################################
################### OUTPUT #######################
##################################################
# Roots in the following methods:

# Bisection: -0.7390851974487305
# Regula-falsi: -0.7390850489536539
# Newton-Raphson: -0.7390851411901728

# Data file for various methods:

# Bisection:
# Iterations Absolute error
# 1 0.5
# 2 0.25
# 3 0.125
# 4 0.0625
# 5 0.03125
# 6 0.015625
# 7 0.0078125
# 8 0.00390625
# 9 0.001953125
# 10 0.0009765625
# 11 0.00048828125
# 12 0.000244140625
# 13 0.0001220703125
# 14 6.103515625e-05
# 15 3.0517578125e-05
# 16 1.52587890625e-05
# 17 7.62939453125e-06
# 18 3.814697265625e-06

# Regula Falsi:
# Iterations Absolute error
# 1 0.13167975861725667
# 2 0.019120951814179277
# 3 0.0024704409584530573
# 4 0.00031356631837975435
# 5 3.970829509136742e-05

# Newton-Raphson:
# Iterations Absolute error
# 0 1.2654645898252153
# 1 0.00455432354418539
