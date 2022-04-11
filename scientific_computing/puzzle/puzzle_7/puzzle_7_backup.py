import matplotlib.pyplot as plt
import numpy as np
import picmod
import time

start = time.time()
img = plt.imread('ceci.jpg')
img = picmod.stretch(img, 1, 0.5)
img = picmod.shift(img, -340, 200)
img = picmod.zoom(img, 2)
plt.style.use('dark_background')
plt.imshow(img)
end = time.time()
print(end-start)
plt.show()
