from library import bisection, regula_falsi, newton_raphson
from math import cos
import matplotlib.pyplot as plt

def f(x):
    return -(x+cos(x))

root0, abs_error0, iterations0 = bisection(f, -2, 0, 1e-6)
abs_error0.remove(0)
iterations0.remove(0)
print("Bisection:", root0)

root1, abs_error1, iterations1 = regula_falsi(f, -2, 0, 1e-6)
abs_error1.remove(0)
iterations1.remove(0)
print("Regula-falsi:", root1)

root2, abs_error2, iterations2 = newton_raphson(f, -2, 1e-6)
print("Newton-Raphson:", root2)

plt.plot(iterations0, abs_error0, label='Bisection')
plt.plot(iterations1, abs_error1, label='Regula Falsi')
plt.plot(iterations2, abs_error2, label='Newton Raphson')
plt.legend()
plt.show()
