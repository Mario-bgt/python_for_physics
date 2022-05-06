import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()

a = 1
x = np.linspace(0,2*np.pi,1000)
y = a*(1-np.cos(x))

plt.plot(x, y, 'ko', markersize=5, color="black")

plt.show()
