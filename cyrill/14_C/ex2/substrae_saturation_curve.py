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
y = [0.064516129,
     0.043478261,
     0.032786885,
     0.026666667,
     0.016806723,
     0.005714286
     ]

plt.plot(x, y, linestyle='dashed', color="black")
plt.errorbar(x=x, y=y, fmt='ok', elinewidth=0.5, markersize=4, capsize=1, color="black")
plt.ylabel(r'$Emerging\:rate\:[1/s]$')
plt.xlabel(r'$Substrate\:concentration\:[mol/L]$')
plt.title(r'$Substrate\:saturation\:curve$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('substrate_saturation_curve.pdf')
plt.show()
