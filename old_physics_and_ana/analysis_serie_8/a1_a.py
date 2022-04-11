import matplotlib.pyplot as plt
import numpy as np
import scipy.special


# natural numbers from 0 to 30
c = np.linspace(-1, 1, 400)
b = np.linspace(-2, -1, 400)
e = np.linspace(1, 2, 400)


n = -1
m =  0.5

# calc all values for y
y = b**2 -n*b + m
z = (n+m)*c
a = e**2 + n*e - m

# finally plot graph
fig = plt.figure()
plt.plot(b, y, linewidth=0.5, color="black")
#plt.plot(x, y, 'ro')
plt.plot(c, z, linewidth=0.5, color="green")
#plt.plot(x, z, 'yo')
plt.plot(e, a, linewidth=0.5, color="yellow")
plt.tick_params(bottom=False, left=False)
plt.title('plot A1')
plt.savefig('s8_a1_b.pdf')
plt.show()