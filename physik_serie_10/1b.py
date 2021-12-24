import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

m = 0.34
roh = 2700
x = np.linspace(-0.02, 0.02,200)
y = x + 2*m*x

plt.plot(x, y, 'k', linewidth=0.5, linestyle='--', label=r'$F( \varepsilon )= \rho +  \varepsilon +2 \mu \cdot \varepsilon  $')
plt.ylabel(r'$\frac{\bigtriangleup R}{R}$')
plt.xlabel(r'$ \varepsilon $')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='upper left')
print(y)
plt.show()
