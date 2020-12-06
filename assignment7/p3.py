from library import shooting_method
import matplotlib as mpl
import matplotlib.pyplot as plt

# # Save plot as pdf
# mpl.use("PDF")

e = 2.71828

def d2ydx2(x, y, z):
    return 1 + z

def dydx(x, y, z):
    return z

x1, y1 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 0.5)
x2, y2 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 0.1)
x3, y3 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 0.05)
x4, y4 = shooting_method(d2ydx2, dydx, 0, 1, 1, 2*(e-1), 0, 0.02)

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.show()

# plt.title("Solution for $y'' = y' + 1$")
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.plot(x, y, label='numerical')
# plt.legend()
# plt.show()

# plt.savefig("plot_3.pdf")


##################################################
################ OUTPUT #########################
##################################################
# Plot file is "plot_3.pdf"

# Guesses for z:
# zeta_h =  1.0 (value overshoots)
# zeta_l =  0.0 (value undershoots)
