import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [0.877192982,
     1.515151515,
     2.380952381,
     3.322259136,
     5.555555556,
     16.66666667
     ]
y = [15.5,
     23,
     30.5,
     37.5,
     59.5,
     175
     ]
xerr = np.linspace(0, 0, len(x))
plt.errorbar(x=x, y=y, xerr=xerr, fmt='ok', elinewidth=0.5, markersize=2, capsize=1, color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace(" ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black',
         label=r'$f(x) = $' + str(slope_intercept))
plt.ylabel(r'$Time\:[s]$')
plt.xlabel(r'$1/[S]$')
plt.title(r'$Linewaver-Burk\:plots$')
plt.legend(loc='best')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('Linewaver_burk_plot.pdf')
plt.show()
