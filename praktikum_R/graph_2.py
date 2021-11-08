import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [0, 1.885834, 3.77167, 5.657499, 7.5434, 9.429167,11.315]
labelx = [r'$t_0$',r'$t_1$',r'$t_2$',r'$t_3$',r'$t_4$',r'$t_5$',r'$t_6$']
ytemp = [10, 9, 7.9, 6.9, 6.0, 5.1,4.2 ]
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
plt.savefig('graph_2.pdf')
plt.show()
print(slope_intercept)
