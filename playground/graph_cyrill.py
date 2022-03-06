import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.linspace(0.1,10,1000)
y = 0.1/x**2-3/x

plt.plot(x, y, 'ko', markersize=5, color="black")
plt.ylabel(r'$\ln(A_i)$')
plt.xlabel(r'$t\:(min)$')
plt.title(r'$Deflection\:as\:function\:of\:time.$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.show()
