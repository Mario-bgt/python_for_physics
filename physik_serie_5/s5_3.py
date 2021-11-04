import matplotlib.pyplot as plt
import numpy as np

g = 10
m = 1
m2 = 2
m3 = 0.5
m4 = 4
m5 = 0.25

x = np.linspace(0, 2*np.pi, 10000)
y = 3*m*g*(1+np.cos(x))
z = 3*m2*g*(1+np.cos(x))
a = 3*m3*g*(1+np.cos(x))
b = 3*m4*g*(1+np.cos(x))
c = 3*m5*g*(1+np.cos(x))

fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, z, linewidth=0.5, color="black")
plt.plot(x, a, linewidth=0.5, color="black")
plt.plot(x, b, linewidth=0.5, color="black")
plt.plot(x, c, linewidth=0.5, color="black")
plt.tick_params(bottom=False, left=False)
plt.title('Fn(winkel)')
plt.savefig('s5_3.pdf')
print(y)
plt.show()
