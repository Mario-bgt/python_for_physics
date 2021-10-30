import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = [1.30264177701689, 1.57084444444444, 2.04871511111111]
y = [0.345, 0.391, 0.524]
yerr = [0.01, 0.01, 0.01]
xerr = [0.029310597604849, 0.0188797370102964, 0.0118509272727448]

bestfit1y = [0.335, 0.381, 0.514]
bestfit2y = [0.355, 0.401, 0.534]
bestfit1x = [1.30264177701689, 2.04871511111111]
bestfit3y = [0.335, 0.534]
bestfit4y = [0.355, 0.514]

plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='k:', linewidth=0.5, capsize=2, elinewidth=0.5, color="black", label='T^2 / l')
plt.plot(x, bestfit1y, color='red', linewidth=0.2)
plt.plot(x, bestfit2y, color='red', linewidth=0.2)
plt.plot(bestfit1x, bestfit3y, color='green', linewidth=0.2)
plt.plot(bestfit1x, bestfit4y, color='green', linewidth=0.2)
plt.ylabel('length in m')
plt.xlabel('T squared')
plt.title('Example graph for error calculus')
plt.tick_params(bottom=False, left=False)

plt.legend(loc='lower right')
plt.savefig('matplotlib.pdf')
plt.show()