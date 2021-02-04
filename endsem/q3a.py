## Using least-square method to fit data from file 'q3data.txt' and fit with
## linear function omega(t) = omega_0 + omega_c * t

# Imports
from library import read_data, linear_fit, pearson_r
import matplotlib.pyplot as plt
import numpy as np      # For plotting curve fit

# Read the data file and store x and y datapoints
xvals, yvals = read_data('q3_data.dat')

# Linear fit for the above datapoints
fit_params = linear_fit(xvals, yvals)

# Extract intercept omega_0 and slope omega_c
omega_0, omega_c = fit_params[0], fit_params[1]
print("omega_0 = {} and omega_c = {}".format(omega_0, omega_c))

# Quality of fit for above set of data points (Pearson's r)
pearson_r = pearson_r(xvals, yvals)
print("The quality of fit, Pearson's r = ", pearson_r)

# Plot the datapoints and fitted function
t = np.linspace(-0.25, 3.5, 100)
omega_t = omega_0 + omega_c * t
plt.plot(t, omega_t, label='Linear fit')
plt.scatter(xvals, yvals, label='Data points')
plt.xlabel("Time $t$")
plt.ylabel("$\omega (t)$")
plt.title("Deceleration of rotating disc")
plt.legend()
plt.show()

###########################################################################
############################ OUTPUT #######################################
###########################################################################
# omega_0 = 2.029102564102564 and omega_c = -0.47470862470862485
# The quality of fit, Pearson's r =  0.9851557666128383
