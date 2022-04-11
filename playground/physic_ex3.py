import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

e_0 = 8.85418782e-12
l = 0.3
m = 0.001
g= 9.81
pi = np.pi
x = np.linspace(0, 9.664e-8, 500)
y = np.cbrt((l*x**2)/(2*pi*e_0*m*g))

plt.plot(x, y, linestyle='dashed', color="black", label= r'$d(Q)\cong  \sqrt[3]{\frac{Q^2\cdot l}{2\cdot \pi \cdot \epsilon_0 \cdot m \cdot g}} $')
plt.ylabel(r'$Distance\:d\:of\:the\:balls\:[m]$')
plt.xlabel(r'$Electronic\:charge\:on\:the\:balls\:[C]$')
plt.title(r'$Exersice\:3b)$')
plt.legend(loc='best')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('physics_kac.pdf')
plt.show()
