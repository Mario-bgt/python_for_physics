import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

ytemp = [0.146,
0.105,
0.078,
0.064,
0.049,
0.041,
0.028,
0.024,
0.018,
]
x = [300,
613.6666667,
927.3333333,
1241,
1554.666667,
1868.333333,
2182,
2495.666667,
2809.333333,
]
y = np.log(ytemp)


plt.plot(x, y, 'ko', markersize=5, color="black")
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