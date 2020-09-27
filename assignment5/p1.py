# Question 1
from library import bisection
from math import sin, log

# Function definition
def f(x):
    return log(x) - sin(x)

root1 = bisection(f, 1.5, 2.5, 1e-6)
print("Bisection: ", root1)
