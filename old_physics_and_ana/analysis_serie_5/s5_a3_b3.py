import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(0, 4000, 4001)

# def y
y = (np.power(-2,x)/(np.power(x,2)+1))

# setting the axes at the centre
fig = plt.figure()

plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('np.power(-2,x)/(np.power(x,2)+1)')
plt.savefig('ana_3_b3.pdf')
print(y)
plt.show()
