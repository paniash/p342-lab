## Plots RMS radial vs \sqrt{N}
# Imports
from walker import *

N = (250, 500, 750, 1000, 1500)

rms_vals = []   # holds RMS distances for each N
root_n_vals = []    # holds radial distances for each N
for i in N:
    rms_vals.append(eval_averages(i)[0])
    root_n_vals.append(sqrt(i))

plt.plot(root_n_vals, rms_vals)
plt.xlabel('$\\sqrt{N}$')
plt.ylabel('$R_{RMS}$')
plt.title('Plot of $R_{RMS}$ vs $\\sqrt{N}$')
plt.show()
plt.savefig('rms-vs-rootn.pdf')
