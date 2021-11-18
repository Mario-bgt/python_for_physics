import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

y = [3,
9.1,
18.2,
27.6,
34,
35.5,
32.1,
25.2,
17.8,
12,
10,
11.5,
16.5,
22,
26.7,
29,
28.3,
25.1,
21,
17.1,
15.2,
14.2,
16.1,
19.5,
22.8,
25.3,
25.8,
24.5,
22.1,
19.5,
17.5,
16.6,
17.2,
18.9,
21.1,
22.9,
23.6,
23.3,
22.3,
20.6,
19.1,
18.1,
18,
18.8,
20.1,
21.5,
22.3,
22.6,
22.2,
21.3,
20.1,
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
z = [20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9,
     20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9,
     20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9, 20.9]
ytemp = [0,40]
i = 5
j = 5.227777778

t1 = [i, i]
t2 = [i+j, i+j]
t3 = [i+2*j, i+2*j]
t4 = [i+3*j, i+3*j]
t5 = [i+4*j, i+4*j]
t6 = [i+5*j, i+5*j]
t7 = [i+6*j, i+6*j]
t8 = [i+7*j, i+7*j]
t9 = [i+8*j, i+8*j]

plt.plot(x, y, 'kx', markersize=5, color="black")
plt.plot(x, y, 'k', linewidth=0.5, linestyle='--')
plt.plot(x, z, 'r', linewidth=0.5, linestyle='-')
plt.plot(t1, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t2, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t3, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t4, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t5, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t6, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t7, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t8, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.plot(t9, ytemp, 'g', linewidth=0.5, linestyle='-')
plt.ylabel(r'$Amplitude\:in\:cm$')
plt.xlabel(r'$time\:in\:min$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1_evaluation.pdf')
plt.show()
