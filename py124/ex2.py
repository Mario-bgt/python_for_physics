import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True


pi = np.pi
E_m = 1
v_0 = 0.5
R = 1

x = np.linspace(0, R, 10000)
y = (E_m*x)/R
z = (v_0/2)*(3-(x**2)/(R**2))
x2 = np.linspace(R, R*5, 10000)
y2 = (E_m*R**2)/(x2**2)
z2 = (v_0*R)/x2

fig = plt.figure()
plt.plot(x, y, 'r', linewidth=0.5, linestyle='--', label=r'$E(r)$')
plt.plot(x2, y2, 'r', linewidth=0.5, linestyle='--')
plt.plot(x, z, 'g', linewidth=0.5, linestyle='--', label=r'$V(r)$')
plt.plot(x2, z2, 'g', linewidth=0.5, linestyle='--')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.ylabel(r'$E(r)\:V(r)$')
plt.xlabel(r'$Distance\:from\:center$')
plt.title(r'$Physics\:homework\:exercise\:2$')
plt.legend(loc='best')
plt.savefig('graph_2.pdf')
plt.show()
