#  _____ _ _ _                 _     _
# | ____| | (_)_ __  ___  ___ (_) __| |
# |  _| | | | | '_ \/ __|/ _ \| |/ _` |
# | |___| | | | |_) \__ \ (_) | | (_| |
# |_____|_|_|_| .__/|___/\___/|_|\__,_|
#             |_|
#            _   _                 _   _
#   ___  ___| |_(_)_ __ ___   __ _| |_(_) ___  _ __
#  / _ \/ __| __| | '_ ` _ \ / _` | __| |/ _ \| '_ \
# |  __/\__ \ |_| | | | | | | (_| | |_| | (_) | | | |
#  \___||___/\__|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|

# Imports
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random

# Define ellipsoid function
def ellipsoid(x, y, z, a, b, c):
    return x**2/a**2 + y**2/b**2 + z**2/c**2 - 1

# Define monte-carlo function for estimating volume
def monte_carlo(N, a, b, c):
    '''Returns the estimated volume and corresponding total points N
    '''
    xrand = []
    yrand = []
    zrand = []
    hits = 0
    for i in range(N):
        xrand.append(random.uniform(-a, a))
        yrand.append(random.uniform(-b, b))
        zrand.append(random.uniform(-c, c))

        if ellipsoid(xrand[i], yrand[i], zrand[i], a, b, c) <= 0:
            hits += 1

    estimated_volume = hits/N * a * b * c * 8

    return estimated_volume, N

# Returns list of estimated volumes as a function of N
def list_volumes(steps, a, b, c):
    vol_list = []
    for n in steps:
        vol, n = monte_carlo(n, a, b, c)
        vol_list.append(vol)

    return vol_list, steps

# Function to return points to cover volume
def ellipsoid_volume(N, a, b, c):
    # Random points within the cuboidal enclosure
    xrand = []
    yrand = []
    zrand = []

    # Hit points (land within the ellipsoid volume)
    x_vol = []
    y_vol = []
    z_vol = []
    for i in range(N):
        xrand.append(random.uniform(-a, a))
        yrand.append(random.uniform(-b, b))
        zrand.append(random.uniform(-c, c))

        if ellipsoid(xrand[i], yrand[i], zrand[i], a, b, c) <= 0:
            x_vol.append(xrand[i])
            y_vol.append(yrand[i])
            z_vol.append(zrand[i])

    return x_vol, y_vol, z_vol

# Function to return fractional error as a function of N
def frac_error(steps, a, b, c):
    error = []   # holds fractional errors for each N
    for n in steps:
        vol, n = monte_carlo(n, a, b, c)
        error.append((vol-12.566)/12.566)

    return error, steps
