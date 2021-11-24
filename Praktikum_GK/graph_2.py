import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

ytemp = [14.6,
10.5,
7.8,
6.4,
4.9,
4.1,
2.8,
2.4,
1.8,

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
y = np.log10(ytemp)

t1 = [y[0],0]
t2 = [y[1], 0]
t3 = [y[2], 0]
t4 = [y[3], 0]
t5 = [y[4], 0]
t6 = [y[5], 0]
t7 = [y[6], 0]
t8 = [y[7], 0]
t9 = [y[8], 0]
x1 = [x[0],x[0]]
x2 = [x[1],x[1]]
x3 = [x[2],x[2]]
x4 = [x[3],x[3]]
x5 = [x[4],x[4]]
x6 = [x[5],x[5]]
x7 = [x[6],x[6]]
x8 = [x[7],x[7]]
x9 = [x[8],x[8]]

plt.plot(x, y, 'ko', markersize=5, color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace("  ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black')
plt.plot(x1,t1, 'k', linewidth=0.5, linestyle='-')
plt.plot(x2,t2, 'k', linewidth=0.5, linestyle='-')
plt.plot(x3,t3, 'k', linewidth=0.5, linestyle='-')
plt.plot(x4,t4, 'k', linewidth=0.5, linestyle='-')
plt.plot(x5,t5, 'k', linewidth=0.5, linestyle='-')
plt.plot(x6,t6, 'k', linewidth=0.5, linestyle='-')
plt.plot(x7,t7, 'k', linewidth=0.5, linestyle='-')
plt.plot(x8,t8, 'k', linewidth=0.5, linestyle='-')
plt.plot(x9,t9, 'k', linewidth=0.5, linestyle='-')
plt.ylabel(r'$\log(A_i)$')
plt.xlabel(r'$t\:(seconds)$')
plt.title(r'$Deflection\:as\:function\:of\:time.$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1_evaluation.pdf')
plt.show()
