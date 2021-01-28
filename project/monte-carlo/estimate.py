# Imports
from ellipsoid import *
import numpy as np

# Define semi-axes
a = 1.0
b = 1.5
c = 2.0
N_max = 50000

# Range of steps N to be taken while estimating the area
steps = [ i for i in range(500, N_max, 100) ]

y, x = list_volumes(steps, a, b, c)
plt.plot(x, y, label='Estimated volume')

exact_x = np.linspace(0, 50000, 100)
exact_y = np.ones(100) * 12.566
plt.plot(exact_x, exact_y, label='Exact volume = 12.566 units$^3$')
plt.xlabel('Number of steps $N$')
plt.ylabel('Estimated volume of ellisoid $V$')
plt.title('Estimation of the volume of ellipsoid using Monte-Carlo')
plt.legend()
plt.show()
