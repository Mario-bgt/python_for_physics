import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,200)
y = np.e**(x**2+7)

plt.plot(x, y)
plt.show()
