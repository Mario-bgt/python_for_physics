import numpy as np


M = 0.018
g = 9.81
k = 1.38*10**(-23)
e = np.e
up = np.log((e**((M*g)/k))*0.5)*k
down = M*g
print(up/down)