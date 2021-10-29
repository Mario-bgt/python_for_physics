import matplotlib.pyplot as plt
import numpy as np


def T(n):
    if n == 0:
        return 0
    else:
        return np.sqrt(1 + T(n-1))


# natural numbers from 0 to 951
x = np.linspace(0, 30, 31)

# calc all values for y
y = [T(i) for i in range(0, 31)]

# finally plot graph
fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('plot A2')
plt.savefig('s5_a2.pdf')
print(T(950))
plt.show()
