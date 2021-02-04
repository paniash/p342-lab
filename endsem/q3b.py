## Using least-square method to fit data from file 'q3data.txt' and fit with
## function omega(t) = omega_0 * exp(-omega_c * t)

# Imports
from library import read_data, linear_fit, pearson_r
from math import log, exp
import matplotlib.pyplot as plt
import numpy as np  # For plotting curve fit

# Read the data file and store x and y datapoints
xvals, yvals = read_data('q3_data.dat')

# Taking logarithm of yvals for curve fit
for i in range(len(yvals)):
    yvals[i] = log(yvals[i])

# Linear fit for the above datapoints with function log w(t) = log w_0 - w_c * t
fit_params = linear_fit(xvals, yvals)

# Extract intercept log w_0 and slope -w_c
intercept, slope = fit_params[0], fit_params[1]
omega_0 = exp(intercept)
omega_c = -slope
print("omega_0 = {} and omega_c = {}".format(omega_0, omega_c))

# Quality of fit for above set of data points (Pearson's r)
quality = pearson_r(xvals, yvals)
print("Pearson's r =", quality)

# Reverting back to original set of yvals
for i in range(len(yvals)):
    yvals[i] = exp(yvals[i])

# Plot the datapoints and fitted function
t = np.linspace(-0.25, 3.5, 100)
omega_t = omega_0 * np.exp(-omega_c * t)
plt.plot(t, omega_t, label='Curve fit')
plt.scatter(xvals, yvals, label='Data points')
plt.xlabel("Time $t$")
plt.ylabel("$\omega (t)$")
plt.title("Deceleration of rotating disc")
plt.legend()
plt.show()


###########################################################################
############################ OUTPUT #######################################
###########################################################################
# omega_0 = 2.2040080182882553 and omega_c = 0.39559617454855667
# Pearson's r = 0.9991179387307721
