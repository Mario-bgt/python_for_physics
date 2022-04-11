import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(-40, 40, 81)

# def y
y = (x**3)
z = (3*x**2)
a = (6*x)


# setting the axes at the centre
fig = plt.figure()

plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, z, linewidth=0.5, color="purple")
plt.plot(x, a, linewidth=0.5, color="blue")
plt.tick_params(bottom=False, left=False)
plt.title('1/np.power(scipy.special.factorial(x),(1/x))')
plt.savefig('s6_a2_c.pdf')
print(y)
plt.show()
