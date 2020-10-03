# Question 1a
from library import bisection, newton_raphson, regula_falsi, write_table, print_table, sin
from math import log
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return log(x) - sin(x)

root0, abs_error0, iterations0  = bisection(f, 1.5, 2.5, 1e-6)
print("Bisection: ", root0)
abs_error0.remove(0)
iterations0.remove(0)

root1, abs_error1, iterations1 = regula_falsi(f, 1.5, 2.5, 1e-6)
abs_error1.remove(0)
iterations1.remove(0)
print("Regula-falsi:", root1)

root2, abs_error2, iterations2 = newton_raphson(f, 1.5, 1e-6)
print("Newton:", root2)

table0 = write_table('bisection_b.csv', iterations0, abs_error0)
table1 = write_table('regula_falsi_b.csv', iterations1, abs_error1)
table2 = write_table('newton_raphson_b.csv', iterations2, abs_error2)

print("\nBisection: ")
print_table(table0)

print("\nRegula Falsi: ")
print_table(table1)

print("\nNewton-Raphson: ")
print_table(table2)

plt.plot(iterations0, abs_error0, label="bisection")
plt.plot(iterations1, abs_error1, label="regular-falsi")
plt.plot(iterations2, abs_error2, label="newton-raphson")
plt.legend()
plt.show()
