# Imports
from walker import *

# Evaluates the R_rms, radial distance and average displacements along x and y directions
N = (250, 500, 750, 1000, 1500)

for i in N:
    rms, radial, avg_x, avg_y = eval_averages(i)
    print("N = {}".format(i))
    print("RMS distance = {} units; Radial distance = {} units".format(rms, radial))
    print("Average displacements along: x = {} units, y = {} units".format(avg_x, avg_y))
    print("\n")
