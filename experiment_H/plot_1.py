import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()
x = [8, 7, 6, 5, 4, 3, 2, 1]
y = [11.86, 11.23, 10.33, 9.61, 8.3, 6.39, 4.44, 2.21]
xerr = [0.16, 0.14, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02]
yerr = [0.33, 0.31, 0.28, 0.27, 0.23, 0.18, 0.12, 0.06]

plt.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=2.5, capsize=1, color="black",
             label=r'$values$')
plt.ylabel(r'$magnetic\:field\:B$')
plt.xlabel(r'$current\:in\:coil\:U_M$')
plt.grid(color='grey', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.title(r'$Results\:of\:part\:one$')
plt.savefig('plot_1.pdf')
plt.show()