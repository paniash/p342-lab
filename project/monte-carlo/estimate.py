# Imports
from ellipsoid import *


# Define semi-axes
a = 1.0
b = 1.5
c = 2.0
N_max = 50000

# Range of steps N to be taken while estimating the area
steps = [ i for i in range(500, N_max, 100) ]

y, x = list_volumes(steps, a, b, c)
plt.plot(x, y, label='estimate')

exact_x = np.linspace(0, 50000, 100)
exact_y = np.ones(100) * 12.566
plt.plot(exact_x, exact_y, label='exact')
plt.legend()
plt.show()
