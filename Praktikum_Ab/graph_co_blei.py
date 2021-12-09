import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

y = [2151,
1630,
1239,
931,
757,
563,
409,
328,
276,
202,
166,]
x = [0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
]
yerr=[46.55104725,
40.57092555,
35.42597917,
30.77336511,
27.80287755,
24.06241883,
20.61552813,
18.54723699,
17.08800749,
14.76482306,
13.49073756,
]


#plt.plot(x, y, 'ko', markersize=1, color="black")
#plt.plot(x, y, 'r', linewidth=0.5, linestyle='--', label=r'$f(\varphi_2)=\sin^{-1}\left(\frac{z_0}{2r}\right)$')
plt.errorbar(x=x, y=y, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=0.5, capsize=1, color="black",label=r'$\varphi_2\:measured$')
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