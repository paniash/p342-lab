from library import runge_kutta
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Save plot as pdf
mpl.use("PDF")

e = 2.71828

# dy/dx = z ; d2y/dx2 = dz/dx
def d2ydx2(x, y, z):
    return 1 - x - z

def dydx(x, y, z):
    return z

x = np.linspace(-5, 5, 100)
y = 1 + e**(-x) - x**2/2 + 2*x
x0, y0 = runge_kutta(d2ydx2, dydx, 0, 2, 1, 100)
plt.title("Solution using Runge-Kutta")
plt.plot(x0,y0, label='Numerical solution')
plt.plot(x,y, label='Analytical solution')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.show()

plt.savefig("plot_2.pdf")

##################################################
################ OUTPUT #########################
##################################################
# Plot file is "plot_2.pdf"
