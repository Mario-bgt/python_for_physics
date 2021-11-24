import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

y = [-0.179,
-0.118,
-0.027,
0.067,
0.131,
0.146,
0.112,
0.043,
-0.031,
-0.089,
-0.109,
-0.094,
-0.044,
0.011,
0.058,
0.081,
0.074,
0.042,
0.001,
-0.038,
-0.057,
-0.067,
-0.048,
-0.014,
0.019,
0.044,
0.049,
0.036,
0.012,
-0.014,
-0.034,
-0.043,
-0.037,
-0.02,
0.002,
0.02,
0.027,
0.024,
0.014,
-0.003,
-0.018,
-0.028,
-0.029,
-0.021,
-0.008,
0.006,
0.014,
0.017,
0.013,
0.004,
-0.008,
     ]
x = [0,
60,
120,
180,
240,
300,
360,
420,
480,
540,
600,
660,
720,
780,
840,
900,
960,
1020,
1080,
1140,
1200,
1260,
1320,
1380,
1440,
1500,
1560,
1620,
1680,
1740,
1800,
1860,
1920,
1980,
2040,
2100,
2160,
2220,
2280,
2340,
2400,
2460,
2520,
2580,
2640,
2700,
2760,
2820,
2880,
2940,
3000,
     ]
z = [0,0]

i = 5
j = 5.227777778
x3 = np.linspace(0,3000,10000)
y3 = (0.179*np.e**((-1*x3)/1250))*np.cos(((2*np.pi)/625)*x3+np.pi*1.05)


plt.plot(x3, y3, 'r', linewidth=0.5, linestyle='-')
plt.plot(x, y, 'kx', markersize=5, color="black")
plt.plot(x, y, 'k', linewidth=0.5, linestyle='--')

plt.ylabel(r'$Amplitude\:in\:cm$')
plt.xlabel(r'$time\:in\:min$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1_evaluation.pdf')
plt.show()
