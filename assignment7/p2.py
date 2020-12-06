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

x0_1, y0_1 = runge_kutta(d2ydx2, dydx, 0, 2, 1, 5, 0.5)
x0_2, y0_2 = runge_kutta(d2ydx2, dydx, 0, 2, 1, 5, 0.1)
x0_3, y0_3 = runge_kutta(d2ydx2, dydx, 0, 2, 1, 5, 0.05)
x0_4, y0_4 = runge_kutta(d2ydx2, dydx, 0, 2, 1, 5, 0.02)

plt.title("Solution using RK4")

plt.plot(x0_1,y0_1, label='$dx = 0.5$')
plt.plot(x0_2,y0_2, label='$dx = 0.1$')
plt.plot(x0_3,y0_3, label='$dx = 0.05$')
plt.plot(x0_4,y0_4, label='$dx = 0.02$')

x = np.linspace(-5, 5, 100)
y = 1 + e**(-x) - x**2/2 + 2*x
plt.plot(x,y, 'r--', label='Analytical solution')
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
