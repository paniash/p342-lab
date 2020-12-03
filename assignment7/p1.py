from library import *
from math import log
import matplotlib.pyplot as plt

e = 2.71828

def dydx_a(y, x):
    return (y*log(y))/x

def dydx_b(y, x):
    return 6 - (2*y)/x

x1, y1 = forward_euler(dydx_a, e, 2, 100)
x2, y2 = forward_euler(dydx_b, 1, 3, 100)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
