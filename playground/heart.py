import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.linspace(-2,2,1000)
y = np.sqrt(1-(np.abs(x)-1)**2)
y2 = np.arccos(1-np.abs(x))-np.pi


plt.plot(x, y, linestyle='-', color="red", label=r'$f(x)_1 = \sqrt{1-(|x|-1)^2}$')
plt.plot(x, y2, linestyle='-', color="red",label=r'$f(x)_2 = \arccos(1-|x|) - \pi  $')
plt.legend(loc='lower right')
plt.savefig('graph_1_evaluation.pdf')
plt.show()
