import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [4,
     6,
     8,
     9.4
     ]
y = [0,
     44.5,
     29.5,
     28.5
     ]

plt.plot(x, y, linestyle='dashed', color="black")
plt.errorbar(x=x, y=y, fmt='ok', elinewidth=0.5, markersize=4, capsize=1, color="black")
plt.ylabel(r'$1/v\:[s^{-1}]$')
plt.xlabel(r'$pH$')
plt.title(r'$pH\:dependence$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('pH_dependence.pdf')
plt.show()
