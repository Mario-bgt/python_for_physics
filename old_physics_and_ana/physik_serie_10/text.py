import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
x = np.linspace(0, 100)
y = x**2

plt.plot(x, y, 'k', linewidth=0.5, linestyle='--', label=r'$F( \varepsilon )= \rho +  \varepsilon +2 \mu \cdot \varepsilon  $')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='upper left')
print(y)
plt.show()
