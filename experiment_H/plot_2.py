import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()
x = [8, 7, 6, 5, 4, 3, 2, 1]
ytemp = [11.66, 10.93, 9.62, 9.44, 8.09, 6.28, 4.27, 2.3]
xerr = [0.16, 0.14, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02]
yerrtemp = [0.24, 0.23, 0.2, 0.2, 0.17, 0.13, 0.09, 0.05]
y = []
yerr = []
for i in ytemp:
    y.append(i*0.1)
for j in yerrtemp:
    yerr.append(j*0.1)

plt.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=2.5, capsize=1, color="black",
             label=r'$values$')
plt.ylabel(r'$magnetic\:field\:B$')
plt.xlabel(r'$current\:in\:coil\:U_M$')
plt.title(r'$Results\:of\:part\:two$')
plt.grid(color='grey', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.savefig('plot_2.pdf')
plt.show()
