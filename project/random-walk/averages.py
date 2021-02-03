# Imports
from walker import *
import random

random.seed(187)

N = (250, 500, 750, 1000, 1500)

# Evaluates the R_rms, radial distance and average displacements along x and y
# directions, for each N
for i in N:
    rms, radial, avg_x, avg_y = eval_averages(i)
    print("N = {}".format(i))
    print("RMS distance = {} units; Radial distance = {} units".format(rms, radial))
    print("Average displacements along: x = {} units, y = {} units".format(avg_x, avg_y))
    print("\n")


##################################################
################ OUTPUT ##########################
##################################################

# N = 250
# RMS distance = 14.996329530063802 units; Radial distance = 13.606815406802163 units
# Average displacements along: x = -1.803494270130047 units, y = -0.8020535997511564 units


# N = 500
# RMS distance = 23.41105527449546 units; Radial distance = 20.906208777267263 units
# Average displacements along: x = 0.9491793036765036 units, y = -0.12321162071386105 units


# N = 750
# RMS distance = 28.031058709137824 units; Radial distance = 25.059877853674035 units
# Average displacements along: x = -0.319543838158925 units, y = -2.0278782802944453 units


# N = 1000
# RMS distance = 31.846154389461102 units; Radial distance = 28.456826560887734 units
# Average displacements along: x = 0.817465206458073 units, y = -3.056914367810234 units


# N = 1500
# RMS distance = 37.60082953941643 units; Radial distance = 32.945648470651 units
# Average displacements along: x = 0.31871473991481614 units, y = -0.25774053767680744 units
