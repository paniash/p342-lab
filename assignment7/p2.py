from library import runge_kutta
import matplotlib.pyplot as plt
import numpy as np

e = 2.71828

# dy/dx = z ; d2y/dx2 = dz/dx
def d2ydx2(x, y, z):
    return 1 - x - z

def dydx(x, y, z):
    return z

x = np.linspace(-5, 5, 100)
y = 1 + e**(-x) - x**2/2 + 2*x
x0, y0 = runge_kutta(d2ydx2, dydx, 0, 2, 1, 100)
plt.plot(x0,y0, label='numerical')
plt.plot(x,y, label='analytical')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.legend()
plt.show()
