import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [1.14,
     0.66,
     0.42,
     0.301,
     0.18,
     0.06

     ]
y = [0.068965517,
     0.052631579,
     0.031746032,
     0.024691358,
     0.016393443,
     0.006289308

     ]

y2 = [0.060606061,
      0.048780488,
      0.030769231,
      0.025316456,
      0.017391304,
      0.006079027
      ]

y3 = [0.064516129,
      0.043478261,
      0.032786885,
      0.026666667,
      0.016806723,
      0.005714286
      ]
plt.plot(x, y, 'ro--', label=r'$2\cdot 10^{-5} \:\%  \:Inhibitor$')
plt.plot(x, y2, 'bo--', label=r'$4\cdot 10^{-5} \:\%  \:Inhibitor$')
plt.plot(x, y3, 'go--', label=r'$No\:Inhibitor$')
plt.ylabel(r'$Emerging\:rate\:[1/s]$')
plt.xlabel(r'$Substrate\:concentration\:[mol/L]$')
plt.title(r'$Substrate\:saturation\:curve$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.savefig('substrate_saturation_curve2.pdf')
plt.show()
