'''
Solve for xi,
x1 + x3 + 2x4 = 6
x2 - 2x3 = -3
x1 + 2x2 - x3 = -2
2x1 + x2 + 3x3 - 2x4 = 0
'''

# Import custom library
from lib import *

# Read matrix from a.txt and assign it to 'a'
a = read_matrix('a.txt')
b = [6, -3, -2, 0]

partial_pivot(a, b, 4)

u = [[0 for i in range(4)] for j in range(4)]
l = [[0 for i in range(4)] for j in range(4)]

for i in range(4):
    l[i][i] = 1

for j in range(4):
    for i in range(4):
        total = 0
        for k in range(i):
            total += l[i][k] * u[k][j]

        if i == j:
            u[i][j] = a[i][j] - total

        elif i > j:
            l[i][j] = (a[i][j] - total)/u[j][j]

        else :
            u[i][j] = a[i][j] - total

y = [0 for i in range(4)]

for i in range(4):
    total = 0
    for j in range(i):
        total += l[i][j] * y[j]
    y[i] = b[i] - total

x = [0 for i in range(4)]

for i in reversed(range(4)):
    total = 0
    for j in range(i+1, 4):
        total += u[i][j] * x[j]
    x[i] = (y[i] - total)/u[i][i]

print(y)
print(x)
