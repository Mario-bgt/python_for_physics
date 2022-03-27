import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 19, 23, 27, 31, 35, 39, 43]
y = [0, -0.077159081, -0.132117965, -0.154976103, -0.252021892, -0.284387177, -0.284387177, -0.317835111, -0.35244064,
     -0.388286772, -0.425465775, -0.635438863, -0.703097511, -0.865616441, -0.990779584, -1.230730253, -1.376442065,
     -1.547067582]

xerr = np.linspace(2, 2, len(x))
plt.errorbar(x=x, y=y, xerr=xerr, fmt='ok', elinewidth=0.5, markersize=2, capsize=1, color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace("  ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black', label=r'$f(x) = $'+str(slope_intercept))
plt.ylabel(r'$\ln\left(\frac{\alpha_t - \alpha_{\infty}}{\alpha_0 - \alpha_{\infty}}\right)$')
plt.xlabel(r'$\Delta\:t\:[min]$')
plt.title(r'$Measurement\:at\:28\:degrees$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1_evaluation.pdf')
plt.show()
print(slope_intercept)
