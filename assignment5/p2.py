# Question 2
from library import polynomial_solver

roots = polynomial_solver([1, -3, -7, 27, -18], 1.5)
print("The roots are: ")
for i in range(len(roots)):
    print(round(roots[i]), end=", ")
