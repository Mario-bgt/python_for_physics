import matplotlib.pyplot as plt
import numpy as np
import matplotlib

pi = np.pi
Q = 1 * 10 ** (-16)
q = 1.6 * 10 ** (-19)
R = 0.001
e_0 = 8.85418782 * 10 ** (-12)
p = 1.8*10**(-6)

x = np.linspace(0, 1, 100)
y = (p*x)/(3*e_0)

x2 = np.linspace(1, 2, 100)
y2 = (p*R**3)/(3*e_0*x**2)

plt.plot(x, y, 'k', linewidth=0.5, linestyle='--')
plt.plot(x2, y2, 'k', linewidth=0.5, linestyle='--')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_2.pdf')
plt.show()
