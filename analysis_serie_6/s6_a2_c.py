import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(0, 40000, 40001)

# def y
y = 1/np.power(scipy.special.factorial(x),(1/x))


# setting the axes at the centre
fig = plt.figure()

plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('1/np.power(scipy.special.factorial(x),(1/x))')
plt.savefig('s6_a2_c.pdf')
print(y)
plt.show()
