import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

B = [5.5, 6, 6.3, 6.7, 7.2, 7.5]
y = [350,400,450,500,550,600]
x = []
for i in B:
    i = i*0.001
    x.append((i**2))
print(x)

plt.plot(x, y, 'ko', markersize=5, color="black")
slope_intercept = np.polyfit(x, y, 1)
print(slope_intercept)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black',
         label=r'$f(x) = 9.523\cdot 10^6 x + 64$')
plt.ylabel(r'$U_A\:(V)$')
plt.xlabel(r'$B^2\:(T^2)$')
plt.title(r'$B^2\:plottet \:against\: U_A$')
plt.legend(loc='best')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph.pdf')
print(x,y)
plt.show()

