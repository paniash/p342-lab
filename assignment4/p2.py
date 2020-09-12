'''
Given the matrix:
    0 2 8 6
    0 0 1 2
    0 1 0 1
    3 7 1 0

Verify if the inverse exists and if it does, then find it.
'''

# Import all functions from custom library
from library import *

# Read matrix 'A' from file 'a2.txt'
A = read_matrix('a2.txt')

# Check if determinant is non-zero and hence compute inverse, else exit.
det = determinant(A.copy())
if det != 0:
    print("Inverse exists!\n")

    # Define the identity matrix 'b'
    b = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        b[i][i] = 1

    # Make copies of matrix 'A' to partial pivot separately with each row of matrix 'b'
    A0 = A.copy()
    A1 = A.copy()
    A2 = A.copy()
    A3 = A.copy()

    # Partial pivot matrix 'A' separately with each row of matrix 'b'
    partial_pivot(A0, b[0], 4)
    partial_pivot(A1, b[1], 4)
    partial_pivot(A2, b[2], 4)
    partial_pivot(A3, b[3], 4)

    # xi is the ith column of the inverted matrix
    x0 = lin_solver(A0, b[0])
    x1 = lin_solver(A1, b[1])
    x2 = lin_solver(A2, b[2])
    x3 = lin_solver(A3, b[3])

    # Store all the column vectors as rows in matrix 'x'
    x = []
    x.append(x0)
    x.append(x1)
    x.append(x2)
    x.append(x3)

    # Transpose matrix 'x' to obtain inverted matrix
    A_inv = [[0 for i in range(4)] for j in range(4)]   # stores the inverse of matrix A
    for j in range(4):
        for i in range(4):
            A_inv[i][j] = round(x[j][i], 2)

    print("The inverse matrix is\n")
    mat_print(A_inv)

else:
    print("Inverse does NOT exist.")
    exit()


'''
Output:
    Inverse exists!

    The inverse matrix is

    [-0.25, 1.67, -1.83, 0.33]
    [0.08, -0.67, 0.83, 0.0]
    [0.17, -0.33, -0.33, 0.0]
    [-0.08, 0.67, 0.17, 0.0]
'''
