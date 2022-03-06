import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

v = np.e**(1/np.e)

x = np.linspace(2, 3, 100000)
y = x**(1/x)
y2 = np.linspace(v, v, 100000)

plt.plot(x, y, linestyle='-', color="black")
plt.plot(x, y2, linestyle='-', color="red")
plt.ylabel(r'$\ln(A_i)$')
plt.xlabel(r'$t\:(min)$')
plt.title(r'$Deflection\:as\:function\:of\:time.$')
plt.legend(loc='upper right')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.show()