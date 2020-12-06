from library import runge_kutta
import matplotlib.pyplot as plt
import numpy as np

e = 2.71828

def d2ydx2(x, y, z):
    return 2*y

def dydx(x, y, z):
    return z

def lagrange_interpolation(zeta_h, zeta_l, yh, yl, y):
    zeta = zeta_l + (zeta_h - zeta_l) * (y - yl)/(yh - yl)
    return zeta

def shooting_method(d2ydx2, dydx, x0, y0, xf, yf, z_guess, tol=1e-6):
    """ (x0, y0) is the first boundary condition
    (xf, yf) is the second boundary condition """

    y = runge_kutta(d2ydx2, dydx, 0, 1.2, z_guess, 20)[1]
    yn = y[-1]      # last element of the list (y_n)

    # begin loop
    if abs(yn - yf) > tol:
        if yn > yf :
            zeta_h = z_guess
            yh = yn

            while yn >= yf:
                i = 0
                if i%2 == 0:
                    z_guess = zeta_h + (i/2 + 1)
                else:
                    z_guess = zeta_h - ((i-1)/2 + 1)

                y = runge_kutta(d2ydx2, dydx, 0, 1.2, z_guess, 20)[1]
                yn = y[-1]      # last element of the list (y_n)
                i += 1

            # after the loop, yn < yf
            zeta_l = z_guess
            yl = yn

            # Calculate zeta
            zeta = lagrange_interpolation(zeta_h, zeta_l, yh, yl, yf)

            # Use Runge-Kutta with zeta as guess
            x, y = runge_kutta(d2ydx2, dydx, x0, y0, zeta, 20)

            return x, y

        elif yn < yf:
            zeta_l = z_guess
            yl = yn

            while yn <= yf:
                i = 0
                if i%2 == 0:
                    z_guess = zeta_l + (i/2 + 1)
                else:
                    z_guess = zeta_l - ((i-1)/2 + 1)

                y = runge_kutta(d2ydx2, dydx, 0, 1.2, z_guess, 20)[1]
                yn = y[-1]      # last element of the list (y_n)
                i += 1

            # after the loop, yn < yf
            zeta_h = z_guess
            yh = yn

            # Calculate zeta
            zeta = lagrange_interpolation(zeta_h, zeta_l, yh, yl, yf)

            # Use Runge-Kutta with zeta as guess
            x, y = runge_kutta(d2ydx2, dydx, x0, y0, zeta, 20)

            return x, y


    # bang on solution in first try
    else:
        x, y = runge_kutta(dy2dx2, dydx, x0, y0, z_guess, 20)
        return x, y


x, y = shooting_method(d2ydx2, dydx, 0, 1.2, 1, 0.9, -1.5)

x0 = np.linspace(0, 1, 100)
y0 = 0.157*e**(np.sqrt(2) * x0) + 1.043*e**(-np.sqrt(2) * x0)
plt.plot(x, y, label='numerical')
plt.plot(x0, y0, label='analytical')
plt.legend()
