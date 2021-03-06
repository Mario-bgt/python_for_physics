import matplotlib.pyplot as plt
import numpy as np
import picmod
import time

start = time.time()
img = plt.imread('holbein.png')
img = picmod.rotate(img, (3 * np.pi) / 20)
img = picmod.stretch(img, 1, 7)
img = picmod.shift(img, -340, 30)
img = picmod.zoom(img, 8)
plt.style.use('dark_background')
plt.imshow(img)
end = time.time()
print(end-start)
plt.show()
