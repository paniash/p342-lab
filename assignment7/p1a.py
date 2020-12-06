from library import forward_euler
from math import log
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Save plot as pdf
mpl.use("PDF")

e = 2.71828

def dydx_a(y, x):
    return (y*log(y))/x

x1_1, y1_1 = forward_euler(dydx_a, e, 2, 5, 0.5)
x1_2, y1_2 = forward_euler(dydx_a, e, 2, 5, 0.1)
x1_3, y1_3 = forward_euler(dydx_a, e, 2, 5, 0.05)
x1_4, y1_4 = forward_euler(dydx_a, e, 2, 5, 0.02)

plt.title("Forward Euler method for $dy/dx = (y \log y)/x$")

x1 = np.linspace(2, 5, 100)
y1 = e**(x1/2)
plt.plot(x1, y1, 'r--', label='Analytic solution')

plt.plot(x1_1, y1_1, label="$dx = 0.5$")
plt.plot(x1_2, y1_2, label="$dx = 0.1$")
plt.plot(x1_3, y1_3, label="$dx = 0.05$")
plt.plot(x1_4, y1_4, label="$dx = 0.02$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.show()
plt.savefig("plot_1a.pdf")


##################################################
################ OUTPUT #########################
##################################################
# Plot file is "plot_1a.pdf"
