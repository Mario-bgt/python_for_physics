import matplotlib.pyplot as plt
import numpy as np
import scipy.special


# natural numbers from 0 to 30
x = np.linspace(0, 3, 4)

# calc all values for y
y = x**x
z = scipy.special.factorial(x)

# finally plot graph
fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.plot(x, z, linewidth=0.5, color="green")
plt.plot(x, z, 'yo')
plt.tick_params(bottom=False, left=False)
plt.title('plot A1')
plt.savefig('s6_a1_b.pdf')
plt.show()
