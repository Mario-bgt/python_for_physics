import matplotlib.pyplot as plt
import numpy as np
import scipy.special


def T(n):
    if n == 1:
        return 0
    else:
        return np.sqrt(1+(n - 1))


# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(0, 10000000, 10000001)

# def y
y = [T(i) for i in range(1, 10000002)]

# setting the axes at the centre
fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('plot A2')
plt.savefig('a2.pdf')
plt.show()
