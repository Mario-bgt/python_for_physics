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

y2 = [14.5,
      19,
      31.5,
      40.5,
      61,
      159
      ]

y3 = [16.5,
      20.5,
      32.5,
      39.5,
      57.5,
      164.5
      ]

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='green')
slope_intercept = np.polyfit(x, y2, 1)
slope_intercept = str(slope_intercept)
print(slope_intercept)
slope_intercept = slope_intercept.replace(" ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y2, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='red',
         label=r'$Linear\:fit\:f(x) = 9.104x + 8.247$')
slope_intercept2 = np.polyfit(x, y3, 1)
slope_intercept2 = str(slope_intercept2)
slope_intercept2 = slope_intercept2.replace(" ", "x + ")
slope_intercept2 = slope_intercept2.replace("[", "")
slope_intercept2 = slope_intercept2.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y3, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='blue',
         label=r'$Linear\:fit\:f(x) = 9.375x + 7.7938$')
plt.plot(x, y, 'go', label=r'$No\:Inhibitor$')
plt.plot(x, y2, 'ro', label=r'$2\cdot 10^{-5} \:\%  \:Inhibitor$')
plt.plot(x, y3, 'bo', label=r'$4\cdot 10^{-5} \:\%  \:Inhibitor$')
plt.ylabel(r'$Time\:[s]$')
plt.xlabel(r'$1/[S]$')
plt.title(r'$Linewaver-Burk\:plot$')
plt.legend(loc='best')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('Linewaver_burk_plot2.pdf')
plt.show()
