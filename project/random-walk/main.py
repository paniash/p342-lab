## Generates 100 random walks for each N = (250, 500, 750, 1000, 1500)
# Imports
from walker import *

N = (250, 500, 750, 1000, 1500)
total_walks = []  # holds walks for each N (5 elements in total)

for i in N:
    coordinates_walks = [] # holds cumulative x and y coordinates for each N
    for _ in range(100):
        x, y = random_walk(i)
        coordinates_walks.append([x, y])

    total_walks.append(coordinates_walks)

# 5 random walks for N = 250
plt.plot(total_walks[0][0][0], total_walks[0][0][1])
plt.plot(total_walks[0][1][0], total_walks[0][1][1])
plt.plot(total_walks[0][2][0], total_walks[0][2][1])
plt.plot(total_walks[0][3][0], total_walks[0][3][1])
plt.plot(total_walks[0][22][0], total_walks[0][22][1])
plt.title('Random walk for ($N$ = 250)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('walk-250.pdf')

# 5 random walks for N = 500
plt.plot(total_walks[1][0][0], total_walks[1][0][1])
plt.plot(total_walks[1][1][0], total_walks[1][1][1])
plt.plot(total_walks[1][2][0], total_walks[1][2][1])
plt.plot(total_walks[1][3][0], total_walks[1][3][1])
plt.plot(total_walks[1][4][0], total_walks[1][4][1])
plt.title('Random walk for ($N$ = 500)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('walk-500.pdf')

# 5 random walks for N = 750
plt.plot(total_walks[2][0][0], total_walks[2][0][1])
plt.plot(total_walks[2][17][0], total_walks[2][17][1])
plt.plot(total_walks[2][2][0], total_walks[2][2][1])
plt.plot(total_walks[2][32][0], total_walks[2][32][1])
plt.plot(total_walks[2][4][0], total_walks[2][4][1])
plt.title('Random walk for ($N$ = 750)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('walk-750.pdf')

# 5 random walks for N = 1000
plt.plot(total_walks[3][26][0], total_walks[3][26][1])
plt.plot(total_walks[3][27][0], total_walks[3][27][1])
plt.plot(total_walks[3][28][0], total_walks[3][28][1])
plt.plot(total_walks[3][29][0], total_walks[3][29][1])
plt.plot(total_walks[3][30][0], total_walks[3][30][1])
plt.title('Random walk for ($N$ = 1000)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('walk-1000.pdf')

# 5 random walks for N = 1500
plt.plot(total_walks[4][15][0], total_walks[4][15][1])
plt.plot(total_walks[4][49][0], total_walks[4][49][1])
plt.plot(total_walks[4][29][0], total_walks[4][29][1])
plt.plot(total_walks[4][32][0], total_walks[4][32][1])
plt.plot(total_walks[4][40][0], total_walks[4][40][1])
plt.title('Random walk for ($N$ = 1500)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('walk-1500.pdf')
