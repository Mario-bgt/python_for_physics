import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

y = [0,
5,
5.9,
6.9,
7.7,
7.9,
8,
8,
7.9,
7.7,
7.4,
6.7,
6.1,
5.5,
4.8,
4.1,
3.3,
2.6,
1.7,
1.1,
0,
-0.8,
-1.7,
-2.4,
-3.1,
-3.8,
-4.4,
-5.2,
-5.8,
-6.4,
-7,
-7.4,
-7.6,
-7.8,
-8.1,
-8.1,
-8.1,
-7.6,
-6.6,
-5.5,
0,

]
x = [0,
3.2,
4.2,
5.7,
7.4,
8.6,
10,
11.1,
12.2,
13.4,
14.2,
15.1,
15.6,
16.2,
16.7,
17.3,
17.6,
17.7,
18.2,
18.3,
18.3,
18.1,
18,
17.9,
17.7,
17.1,
16.6,
16.3,
15.5,
14.9,
14.5,
13.1,
12.5,
11.3,
10.2,
9.1,
8,
6.4,
4.7,
3.2,
0
]



plt.plot(x, y, 'kx', markersize=5, color="black")
plt.plot(x, y, 'k', linewidth=0.5, linestyle='--')

plt.ylabel(r'$position\:(cm)$')
plt.xlabel(r'$time\:(min)$')
plt.title(r'$Recorded\:marks\:of\:laser\:reflection\:position$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_1.pdf')
plt.show()
