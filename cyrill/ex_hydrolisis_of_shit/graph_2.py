import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [5, 6.5, 7.5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [-0.70849275, -0.85238693, -0.992744288, -1.034708487, -1.33196001, -1.433056127, -1.594324275, -1.817467826,
     -1.950999219, -1.987366863, -2.192161275, -2.392831971, -2.575153528, -2.718254371, -2.798297079, -2.885308456
     ]

xerr = np.linspace(1, 1, len(x))
plt.errorbar(x=x, y=y, xerr=xerr, fmt='ok', elinewidth=0.5, markersize=2, capsize=1, color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace("  ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black',
         label=r'$f(x) = $' + str(slope_intercept))
plt.ylabel(r'$\ln\left(\frac{\alpha_t - \alpha_{\infty}}{\alpha_0 - \alpha_{\infty}}\right)$')
plt.xlabel(r'$\Delta\:t\:[min]$')
plt.title(r'$Measurement\:at\:38\:degrees$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_2_evaluation.pdf')
plt.show()
print(slope_intercept)
