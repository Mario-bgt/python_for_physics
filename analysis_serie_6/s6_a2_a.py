import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(0, 40000, 40001)

#def y
y = []
z = []
a = []
t = np.linspace(1, 40002)
for i in t:
    z = int(np.sqrt(i))
    p = np.power(2, z)
    y.append(p)

# setting the axes at the centre
fig = plt.figure()

plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('np.power(2, -ak)')
plt.savefig('s6_a2_a.pdf')
print(y)
plt.show()
