## To determine Wein's constant using Newton-Raphson method

# Imports
from math import exp
from library import *

# Define Planck's law spectrum function
def planck(x):
    return (x-5) * exp(x) + 5

# Define constants
h = 6.626 * 10**(-34)
k = 1.381 * 10**(-23)
c = 3 * 10**8

sol_x = newton_raphson(planck, 6, 10**(-4))[0]

# Hence, Wein's constant b = (h*c)/(k*sol_x)
b = (h * c)/(k * sol_x)

# Printing Wien's constant
print("Wien's constant = ", b, "m K")


#################################################
################# OUTPUT ########################
#################################################
# Wien's constant =  0.0028990103307379917 m K
