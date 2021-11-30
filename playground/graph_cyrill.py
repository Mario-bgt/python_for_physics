import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

y = [0.60,
14.45,
28.13,
40.45,
53.00,
64.55,
73.80,
]
x = [0.00000,
1.09861,
2.19722,
3.29584,
4.39445,
5.49306,
6.59167,
]
x2 = np.linspace(0, 7, 100)
y2 = np.linspace(0, 0, 100)


plt.plot(x, y, 'ko', markersize=5, color="black")
plt.plot(x2, y2, linestyle='-', color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace("  ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black', label=r'$f(x) = $'+str(slope_intercept))
plt.ylabel(r'$\ln(A_i)$')
plt.xlabel(r'$t\:(min)$')
plt.title(r'$Deflection\:as\:function\:of\:time.$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1_evaluation.pdf')
plt.show()
print(slope_intercept)