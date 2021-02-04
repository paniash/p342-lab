## Boundary value problem using shooting method
## To find the velocity of rocket at time t=0

# Imports
from library import shooting_method

# Define constants
g = 9.8

# Define differential equation: d2y/dt2 = -g
def d2ydt2(t, y, z):
    return -g

# z = dy/dt
def dydt(t, y, z):
    return z

# Define boundary values
t_initial = 0
t_final = 5
y_initial = 2
y_final = 45

# Guesses taken for dy/dx are 10 and 100
t, y, z = shooting_method(d2ydt2, dydt, t_initial, y_initial, t_final, y_final, 10, 100, step_size=0.05)

# Print launch velocity dy/dt at t=0 => z(t=0) = z[0]
print("Launch velocity of the rocket is {} m/s".format(z[0]))


##############################################################
##################### OUTPUT #################################
##############################################################
# Launch velocity of the rocket is 33.09999999999994 m/s
