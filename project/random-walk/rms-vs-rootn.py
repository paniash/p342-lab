# Imports
from walker import *

# Plots RMS radial vs \sqrt{N}
N = (250, 500, 750, 1000, 1500)

rms_vals = []
root_n_vals = []
for i in N:
    rms_vals.append(eval_averages(i)[0])
    root_n_vals.append(sqrt(i))

plt.plot(root_n_vals, rms_vals)
plt.xlabel('$\\sqrt{N}$')
plt.ylabel('$R_{RMS}$')
plt.title('Plot of $R_{RMS}$ vs $\\sqrt{N}$')
plt.show()
