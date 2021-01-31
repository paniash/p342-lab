# Imports
from ellipsoid import *

# Define semi-axes for ellisoid
a = 1.0
b = 1.5
c = 2.0

x, y, z = ellipsoid_volume(10000, a, b, c)

# Plotting volume of ellipsoid
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, s=0.8)
ax.set_title('3D plot of ellisoid ($N$=10000)')
plt.show()
