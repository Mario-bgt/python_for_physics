import numpy as np
import matplotlib.pyplot as plt

def potential(x_0, y_0):
    x = np.linspace(-24-x_0, 24-x_0, 24)
    y = np.linspace(-12-y_0, 12-y_0, 12)
    xx, yy = np.meshgrid(x, y)
    return 1/(np.sqrt(xx**2+yy**2))

img = plt.imread('img.jpg')
for i in range(100):
    plt.imshow(img, extent = (-24, 24, -12, 12))
    plt.contour(potential(-10 + 2*i, 2) + potential(-2,-2), cmap = 'summer', extent = (-24, 24, -12, 12), alpha = 0.5,)
    plt.pause(0.1)
    plt.clf()
plt.show()


