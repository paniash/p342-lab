# Imports
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

#%%
random.seed(1029)

#%%
def rand_walk(N):
    ''' Generates 100 random walks with RMS, radial distance and average
    displacement
    '''
    walk = []
    rms_square = 0
    radial_distance = 0
    avg_x = 0
    avg_y = 0
    for i in range(100):
        x = 0
        y = 0
        pos_x = []
        pos_y = []
        square_total = 0
        for _ in range(N):
            pos_x.append(x)
            pos_y.append(y)
            theta = 2 * pi * random.random()
            dx = cos(theta)
            dy = sin(theta)
            x += dx
            y += dy
            square_total += dx**2 + dy**2

        walk.append([pos_x, pos_y])
        rms_square += square_total/100
        radial_distance += sqrt(x**2 + y**2)/100
        avg_x += x/100
        avg_y += y/100

    rms = sqrt(rms_square)

    return walk, rms, radial_distance, avg_x, avg_y
