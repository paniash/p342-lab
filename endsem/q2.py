## Finding time period T of a pendulum using Simpson's method of integration

# Imports
from library import integrate_simpson
from math import sin, sqrt, pi

# Define limits and other constants
lims = [0, pi/2]
a = sin(pi/8)
g = 9.8
L = 1

# Define function for time period
def time_period(phi):
    return 4 * sqrt(L/g) * 1/sqrt(1 - a**2 * sin(phi)**2)

# Solve for T using Simpson's method
T = integrate_simpson(time_period, lims, N=10)

# Print the time period
print("The time period of the pendulum is {} seconds.".format(T))


##############################################################
##################### OUTPUT #################################
##############################################################
# The time period of the pendulum is 2.0873200174795916 seconds.
