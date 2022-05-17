import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()
x1 = [8, 7, 6, 5, 4, 3, 2, 1]
y1temp = [11.86, 11.23, 10.33, 9.61, 8.3, 6.39, 4.44, 2.21]
xerr1 = [0.16, 0.14, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02]
yerr1temp = [0.33, 0.31, 0.28, 0.27, 0.23, 0.18, 0.12, 0.06]
x2 = [8, 7, 6, 5, 4, 3, 2, 1]
y2temp = [11.66, 10.93, 9.62, 9.44, 8.09, 6.28, 4.27, 2.3]
xerr2 = [0.16, 0.14, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02]
yerr2temp = [0.24, 0.23, 0.2, 0.2, 0.17, 0.13, 0.09, 0.05]
x3 = [8, 7, 6, 5, 4, 3, 2, 1]
y3temp = [11.53, 10.97, 10.23, 9.33, 8, 6.18, 4.26, 2.16]
xerr3 = [0.16, 0.14, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02]
yerr3temp = [0.17533562993584617, 0.1668197623934287, 0.15556665171237696, 0.14188043601920597, 0.1216552506059644, 0.09397868109310749, 0.06478142094767604, 0.032846917663610385]

y1 = []
yerr1 = []
for i in y1temp:
    y1.append(i*0.1)
for j in yerr1temp:
    yerr1.append(j*0.1)
y2 = []
yerr2 = []
for i in y2temp:
    y2.append(i*0.1)
for j in yerr2temp:
    yerr2.append(j*0.1)
y3 = []
yerr3 = []
for i in y3temp:
    y3.append(i*0.1)
for j in yerr3temp:
    yerr3.append(j*0.1)


plt.errorbar(x=x1, y=y1, xerr=xerr1, yerr=yerr1, fmt='.r', elinewidth=0.5, markersize=2.5, capsize=1, color="black",
             label=r'$values\:first\:part$')
plt.errorbar(x=x2, y=y2, xerr=xerr2, yerr=yerr2, fmt='.g', elinewidth=0.5, markersize=2.5, capsize=1, color="black",
             label=r'$values\:second\:part$')
plt.errorbar(x=x3, y=y3, xerr=xerr3, yerr=yerr3, fmt='.b', elinewidth=0.5, markersize=2.5, capsize=1, color="black",
             label=r'$values\:third\:part$')
plt.ylabel(r'$magnetic\:field\:B$')
plt.xlabel(r'$current\:in\:coil\:U_M$')
plt.title(r'$Results\:of\:all\:obtained\:values$')
plt.grid(color='grey', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.savefig('plot_all.pdf')
plt.show()