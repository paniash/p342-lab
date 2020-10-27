import random
import matplotlib.pyplot as plt
from library import monte_carlo

# Define limits
a = 0.0
b = 1.0

# Define function
def f(x):
    return 4/(1+x**2)

# List containing values of N for sampling
nlist = [ i for i in range(10, 3000, 10) ]

# List containing all values of F_n for corresponding vallues of N
flist = []

# Standard deviation
sigma_list = []

for n in nlist:
    answer, xrand = monte_carlo(f, [a, b], n)
    flist.append(answer)

    # Standard deviation
    var = 0
    for i in range(n):
        var += (f(xrand[i]))**2/float(n) - (f(xrand[i])/float(n))**2

    sigma = var**(0.5)
    sigma_list.append(sigma)


# plt.title("Plot of $\pi$ vs $N$")
# plt.plot(nlist, flist)
# plt.xlabel("N")
# plt.ylabel("Estimate of $\pi$")

plt.title("Standard deviation plot")
plt.xlabel("N")
plt.ylabel("$\sigma$")
plt.plot(nlist, sigma_list)
plt.show()
