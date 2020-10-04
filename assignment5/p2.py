# Question 2
from library import polynomial_solver

roots = polynomial_solver([1, -3, -7, 27, -18], 1.5)
print("The roots are: ")
for i in range(len(roots)):
    print(roots[i], end=", ")
print("\nThe rounded roots are: ")
for i in range(len(roots)):
    print(round(roots[i]), end=", ")

##################################################
################### OUTPUT #######################
##################################################
# The roots are:
# 0.9999999999999998, -3.0, 3.0, 2.0,
# The rounded roots are:
# 1, -3, 3, 2,
