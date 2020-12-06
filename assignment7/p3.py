from library import shooting_method
import matplotlib as mpl
import matplotlib.pyplot as plt

# Save plot as pdf
mpl.use("PDF")

e = 2.71828

def d2ydx2(x, y, z):
    return 1 + z

def dydx(x, y, z):
    return z

x, y = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0.0)

plt.title("Solution for $y'' = y' + 1$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.plot(x, y, label='numerical')
plt.legend()
plt.show()

plt.savefig("plot_3.pdf")


##################################################
################ OUTPUT #########################
##################################################
# Plot file is "plot_3.pdf"

# Guesses for z:
# zeta_h =  1.0
# zeta_l =  0.0
