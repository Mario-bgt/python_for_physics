import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [0, 1.91834, 3.8367, 5.755, 7.6734, 9.59167]
labelx = [r'$t_0$',r'$t_1$',r'$t_2$',r'$t_3$',r'$t_4$',r'$t_5$',]
ytemp = [10, 9.2, 8.5, 7.8, 7.1, 6.5]
y = np.log(ytemp)

plt.plot(x, y, 'kx', markersize=5, color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace("  ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black', label=r'$f(x) = $'+str(slope_intercept))
plt.ylabel(r'$\ln\varphi (t)$')
plt.xlabel(r'$time$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='-.', linewidth=0.2)
plt.xticks(ticks=x,labels=labelx)
plt.savefig('graph_1.pdf')
plt.show()
print(slope_intercept)

