import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [100,
     50,
     25,
     0
     ]
y = [0.090909091,
     0.042553191,
     0.037383178,
     0
     ]

plt.plot(x, y, linestyle='dashed', color="black")
plt.errorbar(x=x, y=y, fmt='ok', elinewidth=0.5, markersize=4, capsize=1, color="black")
plt.ylabel(r'$Emerging\:rate\:[1/s]$')
plt.xlabel(r'$Enzyme\:concentration\:[mol/L]$')
plt.title(r'$Experiment\:1$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('experiment_1.pdf')
plt.show()
