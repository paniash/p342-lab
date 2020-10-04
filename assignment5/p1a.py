# Question 1a
from library import bisection, newton_raphson, regula_falsi, write_table, print_table, sin, log
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("PDF")   # renders the plots in pdf format

# Function definition
def f(x):
    return log(x) - sin(x)

print("Roots in the following methods:\n")
root0, abs_error0, iterations0  = bisection(f, 1.5, 2.5, 1e-6)
print("Bisection: ", root0)
abs_error0.remove(0)
iterations0.remove(0)

root1, abs_error1, iterations1 = regula_falsi(f, 1.5, 2.5, 1e-6)
abs_error1.remove(0)
iterations1.remove(0)
print("Regula-falsi:", root1)

root2, abs_error2, iterations2 = newton_raphson(f, 1.5, 1e-6)
print("Newton-Raphson:", root2)

table0 = write_table('bisection_a.csv', iterations0, abs_error0)
table1 = write_table('regula_falsi_a.csv', iterations1, abs_error1)
table2 = write_table('newton_raphson_a.csv', iterations2, abs_error2)

print("\nData file for various methods: \n")
print("Bisection: ")
print_table(table0)

print("\nRegula Falsi: ")
print_table(table1)

print("\nNewton-Raphson: ")
print_table(table2)

plt.plot(iterations0, abs_error0, label="Bisection")
plt.plot(iterations1, abs_error1, label="Regular Falsi")
plt.plot(iterations2, abs_error2, label="Newton Raphson")
plt.title("Convergence plot for various methods")
plt.xlabel("Iterations")
plt.ylabel("Absolute error")
plt.legend()
plt.show()
plt.savefig("plot_1a.pdf")

##################################################
################### OUTPUT #######################
##################################################
# Roots in the following methods:

# Bisection:  2.2190771102905273
# Regula-falsi: 2.2190771251098753
# Newton-Raphson: 2.2190771321756997

# Data file for various methods:

# Bisection:
# Iterations Absolute error
# 1 0.25
# 2 0.125
# 3 0.0625
# 4 0.03125
# 5 0.015625
# 6 0.0078125
# 7 0.00390625
# 8 0.001953125
# 9 0.0009765625
# 10 0.00048828125
# 11 0.000244140625
# 12 0.0001220703125
# 13 6.103515625e-05
# 14 3.0517578125e-05
# 15 1.52587890625e-05
# 16 7.62939453125e-06
# 17 3.814697265625e-06

# Regula Falsi:
# Iterations Absolute error
# 1 0.06359020706238949
# 2 0.004499521795959804
# 3 0.00030703493542594273
# 4 2.0896934607606e-05

# Newton-Raphson:
# Iterations Absolute error
# 0 0.9933956435244631
# 1 0.2586540253061922
# 2 0.01559647994963731
