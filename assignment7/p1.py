from library import forward_euler
from math import log
import matplotlib as mpl
import matplotlib.pyplot as plt

# Save plot as pdf
mpl.use("PDF")

e = 2.71828

def dydx_a(y, x):
    return (y*log(y))/x

def dydx_b(y, x):
    return 6 - (2*y)/x

x1, y1 = forward_euler(dydx_a, e, 2, 100)
x2, y2 = forward_euler(dydx_b, 1, 3, 100)
plt.title("Solution using forward Euler method")
plt.plot(x1, y1, label="$dy/dx = (y \log y)/x$")
plt.plot(x2, y2, label="$dy/dx = 6 - (2y)/x$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.show()

plt.savefig("plot_1.pdf")


##################################################
################ OUTPUT #########################
##################################################
# Plot file is "plot_1.pdf"
