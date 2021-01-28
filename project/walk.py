# Imports
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

#%%
random.seed(1029)

#%%
N = (250, 500, 750, 1000, 1500)

nth_set_walk = []    # contains list of all the coordinates for all the walks

for i in range(len(N)):
    walks = []  # holds coordinates of each walk, as a list, for each N
    for _ in range(100):    # 100 walks for each N
        x = 0    # x coordinate at nth step
        y = 0    # y coordinate at nth step
        pos_x = []  # cumulative list of x coordinates for each N
        pos_y = []  # cumulative list of y coordinates for each N
        square_total = 0   # holds sum of squares for a particular random walk
        for _ in range(N[i]):
            pos_x.append(x)
            pos_y.append(y)
            theta = 2 * pi * random.random()
            dx = cos(theta)
            dy = sin(theta)
            x += dx
            y += dy

        walks.append([pos_x, pos_y])

    nth_set_walk.append(walks)

#%%
for i in range(5):
    plt.plot(nth_set_walk[0][i][0], nth_set_walk[0][i][1])

#%% N = 250
plt.plot(nth_set_walk[0][2][0], nth_set_walk[0][2][1])
plt.plot(nth_set_walk[0][40][0], nth_set_walk[0][40][1])
plt.plot(nth_set_walk[0][80][0], nth_set_walk[0][80][1])
plt.plot(nth_set_walk[0][76][0], nth_set_walk[0][76][1])
plt.plot(nth_set_walk[0][96][0], nth_set_walk[0][96][1])
plt.title('N = 250')
# plt.savefig('walk-250.pdf')


#%% N = 500
plt.plot(nth_set_walk[1][2][0], nth_set_walk[1][2][1])
plt.plot(nth_set_walk[1][44][0], nth_set_walk[1][44][1])
plt.plot(nth_set_walk[1][81][0], nth_set_walk[1][81][1])
plt.plot(nth_set_walk[1][39][0], nth_set_walk[1][39][1])
plt.plot(nth_set_walk[1][96][0], nth_set_walk[1][96][1])
plt.title('N = 500')
# plt.savefig('walk-500.pdf')


#%% N = 750
plt.plot(nth_set_walk[2][1][0], nth_set_walk[2][1][1])
plt.plot(nth_set_walk[2][44][0], nth_set_walk[2][44][1])
plt.plot(nth_set_walk[2][80][0], nth_set_walk[2][80][1])
plt.plot(nth_set_walk[2][76][0], nth_set_walk[2][76][1])
plt.plot(nth_set_walk[2][96][0], nth_set_walk[2][96][1])
plt.title('N = 750')
# plt.savefig('walk-750.pdf')


#%% N = 1000
plt.plot(nth_set_walk[3][2][0], nth_set_walk[3][2][1])
plt.plot(nth_set_walk[3][40][0], nth_set_walk[3][40][1])
plt.plot(nth_set_walk[3][80][0], nth_set_walk[3][80][1])
plt.plot(nth_set_walk[3][75][0], nth_set_walk[3][75][1])
plt.plot(nth_set_walk[3][97][0], nth_set_walk[3][97][1])
plt.title('N = 1000')
# plt.savefig('walk-1000.pdf')


#%% N = 1500
plt.plot(nth_set_walk[4][3][0], nth_set_walk[4][3][1])
plt.plot(nth_set_walk[4][32][0], nth_set_walk[4][32][1])
plt.plot(nth_set_walk[4][81][0], nth_set_walk[4][81][1])
plt.plot(nth_set_walk[4][75][0], nth_set_walk[4][75][1])
plt.plot(nth_set_walk[4][95][0], nth_set_walk[4][95][1])
plt.title('N = 1500')
# plt.savefig('walk-1500.pdf')


#%% Root mean square distance
rms2 =
