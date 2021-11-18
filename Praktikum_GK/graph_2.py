import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

ytemp = [14.6,
10.56,
7.9,
6.4,
7.9,
4.2,
2.6,
2.9,
1.6
]
x = [5,
10.22777778,
15.45555556,
20.68333333,
25.91111111,
31.13888889,
36.36666667,
41.59444444,
46.82222222

]
y = np.log(ytemp)


plt.plot(x, y, 'ko', markersize=5, color="black")
slope_intercept = np.polyfit(x, y, 1)
slope_intercept = str(slope_intercept)
slope_intercept = slope_intercept.replace("  ", "x + ")
slope_intercept = slope_intercept.replace("[", "")
slope_intercept = slope_intercept.replace("]", "")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black', label=r'$f(x) = $'+str(slope_intercept))
plt.ylabel(r'$Amplitude\:in\:cm$')
plt.xlabel(r'$time\:in\:min$')
plt.title(r'$Recorded\:marks\:of\:laser\:reflection\:position$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1_evaluation.pdf')
plt.show()
