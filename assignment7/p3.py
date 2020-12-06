from library import shooting_method
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Save plot as pdf
mpl.use("PDF")

e = 2.71828

def d2ydx2(x, y, z):
    return 1 + z

def dydx(x, y, z):
    return z

x1, y1 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 3.0, 0.5)
x2, y2 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 1.5, 0.1)
x3, y3 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 1.0, 0.05)
x4, y4 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 1.0, 0.02)

x = np.linspace(0, 1, 100)
y = 2*e**x - x - 1

plt.title("Solution using shooting method")
plt.plot(x1, y1, label='$dx = 0.5$')
plt.plot(x2, y2, label='$dx = 0.1$')
plt.plot(x3, y3, label='$dx = 0.05$')
plt.plot(x4, y4, label='$dx = 0.02$')
plt.plot(x, y, 'r--', label='Analytic solution')
plt.legend()
plt.show()


plt.savefig("plot_3.pdf")


##################################################
################ OUTPUT #########################
##################################################
# Plot file is "plot_3.pdf"
