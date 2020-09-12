'''
Solve for the set of linear equations using LU decomposition
    x1 + x3 + 2x4 = 6
    x2 - 2x3 = -3
    x1 + 2x2 - x3 = -2
    2x1 + x2 + 3x3 - 2x4 = 0
'''

# Import all functions from custom library
from library import *

# Read matrix 'a' from file 'a1.txt'
a = read_matrix('a1.txt')
b = [6, -3, -2, 0]

x = lin_solver(a, b)
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])
print("x4 =", x[3])

'''
Output:
    x1 = 1.0
    x2 = -1.0
    x3 = 1.0
    x4 = 2.0
'''
