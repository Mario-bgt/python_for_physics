import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(0, 40, 41)

# def y
# y = (np.sqrt(x+np.sqrt(x))-np.sqrt(x))
#y = (np.power(-2, x)/(np.power(x, 2)+1))
#y = ((1+np.power(-1, x))*((x+1)/(x))+np.power(-1, x))
#y = (scipy.special.factorial(x)/np.power(x, x))
#y = ((np.power(-1, x)*(x+(2/x)-np.sqrt(np.power(x, x)+4*x))))
#y = (np.power(-2, x)/(np.power(x,x)+1))
y = (np.power(-1, x)*(x+(x/2)-np.sqrt(1+(4/x))))

# setting the axes at the centre
fig = plt.figure()

plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('(1+np.power(-1, x))*((x+1)/(x))+np.power(-1, x)')
plt.savefig('ana_1_b.pdf')
plt.show()
