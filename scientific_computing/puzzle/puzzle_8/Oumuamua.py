import numpy as np
import matplotlib.pyplot as plt
from calc import *

e = 1.2
a = 1.28
t = np.linspace(-np.pi, np.pi, 160)
phi_tot = list()
for i in t:
    def f(phi):
        j = e*np.sinh(phi)-phi-i
        return j


    def Df(phi):
        j = e*np.cosh(phi)-1
        return j
    xn = 10
    res = newton(f, Df, xn)
    phi_tot.append(res)


x = a*(e-np.cosh(phi_tot))
y = a*np.sqrt(e**2-1)*np.sinh(phi_tot)


plt.plot(x,y,'y.')
plt.show()





