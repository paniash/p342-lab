## Plots fractional error vs total no. of random points N
from ellipsoid import frac_error
import matplotlib.pyplot as plt

# Define semi-axes
a = 1.0
b = 1.5
c = 2.0
N_max = 50000

# Range of steps N to be taken while estimating the area
steps = [ i for i in range(500, N_max, 100) ]

error, step_number = frac_error(steps, a, b, c)
plt.plot(step_number, error)
plt.title('Fractional error vs $N$')
plt.xlabel('Step number $N$')
plt.ylabel('Fractional error')
plt.show()
