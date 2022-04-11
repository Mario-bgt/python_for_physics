import numpy as np
import matplotlib.pyplot as plt
from calc import *

e = 0.967
a = 17.8
t = np.linspace(0, 2*np.pi, 10000)
phi_tot = list()
for i in t:
    def f(phi):
        j = phi - e * np.sin(phi) - i
        return j


    def Df(phi):
        j = 1 - e * np.cos(phi)
        return j
    xn = 10
    res = newton(f, Df, xn)
    phi_tot.append(res)
    print(i, res)

x = a*(np.cos(phi_tot)-e)
y = a*np.sqrt(1-e**2)*np.sin(phi_tot)


plt.plot(x,y,'y.')
plt.show()




