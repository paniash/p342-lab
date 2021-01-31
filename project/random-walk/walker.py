# Imports
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

random.seed(1029)

def random_walk(N):
    '''Generates a list of x and y coordinates for a random walk with a
    user-specified number of steps N
    '''
    pos_x = 0    # instantaneous x coordinate
    pos_y = 0    # instantaneous y coordinate
    x = []      # list of all the x coordinates of the walk
    y = []      # list of all the y coordinates of the walk
    for _ in range(N):
        x.append(pos_x)
        y.append(pos_y)
        theta = 2 * pi * random.random()
        dx = cos(theta)
        dy = sin(theta)
        pos_x += dx
        pos_y += dy

    return x, y

# Function to return all the averages, i.e. RMS distance, radial distance and
# average displacement of x and y
def eval_averages(N, num_walks=100):
    '''N: number of steps of the walk
    num_walks: number of walks to be averaged over for a given N (user-specified)
    '''
    rms = 0
    rms_square = 0
    radial_distance = 0
    avg_x = 0
    avg_y = 0
    for i in range(num_walks):
        x, y = random_walk(N)
        x_last = x.pop()    # last x coordinate of the walk
        y_last = y.pop()    # last y coordinate of the walk
        rms_square += x_last**2 + y_last**2
        radial_distance += sqrt(x_last**2 + y_last**2)/float(num_walks)
        avg_x += x_last/float(num_walks)
        avg_y += y_last/float(num_walks)

    rms = sqrt(rms_square/float(num_walks))

    return rms, radial_distance, avg_x, avg_y
