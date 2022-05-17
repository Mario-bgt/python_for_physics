import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()
x = [8, 7, 6, 5, 4, 3, 2, 1]
ytemp = [11.53, 10.97, 10.23, 9.33, 8, 6.18, 4.26, 2.16]
xerr = [0.16, 0.14, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02]
yerrtemp = [0.17533562993584617, 0.1668197623934287, 0.15556665171237696, 0.14188043601920597, 0.1216552506059644, 0.09397868109310749, 0.06478142094767604, 0.032846917663610385]
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
plt.title(r'$Results\:of\:part\:three$')
plt.grid(color='grey', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.savefig('plot_3.pdf')
plt.show()
