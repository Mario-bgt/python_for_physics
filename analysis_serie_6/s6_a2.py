import matplotlib.pyplot as plt
import numpy as np


def T(n):
    if n == 0:
        return 1
    else:
        return 1 + 1/T(n-1)


# natural numbers from 0 to 30
x = np.linspace(0, 30, 31)

# calc all values for y
y = [T(i) for i in range(0, 31)]

# finally plot graph
fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('plot A1')
plt.savefig('s6_a1_b.pdf')
print(T(950))
print(y, end='\n')
plt.show()
