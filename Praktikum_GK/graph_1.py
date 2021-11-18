import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

y = [-17.9,
-11.8,
-2.7,
6.7,
13.1,
14.6,
11.2,
4.3,
-3.1,
-8.9,
-10.9,
-9.4,
-4.4,
1.1,
5.8,
8.1,
7.4,
4.2,
0.1,
-3.8,
-5.7,
-6.7,
-4.8,
-1.4,
1.9,
4.4,
4.9,
3.6,
1.2,
-1.4,
-3.4,
-4.3,
-3.7,
-2,
0.2,
2,
2.7,
2.4,
1.4,
-0.3,
-1.8,
-2.8,
-2.9,
-2.1,
-0.8,
0.6,
1.4,
1.7,
1.3,
0.4,
-0.8,
     ]
x = [0, 1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     9,
     10,
     11,
     12,
     13,
     14,
     15,
     16,
     17,
     18,
     19,
     20,
     21,
     22,
     23,
     24,
     25,
     26,
     27,
     28,
     29,
     30,
     31,
     32,
     33,
     34,
     35,
     36,
     37,
     38,
     39,
     40,
     41,
     42,
     43,
     44,
     45,
     46,
     47,
     48,
     49,
     50,
     ]
z = [0,0]
ytemp = [-1,52]


plt.plot(x, y, 'kx', markersize=5, color="black")
plt.plot(x, y, 'k', linewidth=0.5, linestyle='--')
plt.plot(ytemp, z, 'k', linewidth=0.5, linestyle='-')
plt.ylabel(r'$Amplitude\:in\:cm$')
plt.xlabel(r'$time\:in\:min$')
plt.title(r'$Recorded\:marks\:of\:laser\:reflection\:position$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1.pdf')
plt.show()
