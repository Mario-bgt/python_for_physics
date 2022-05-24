import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import arccos


r = 123
p_phi = 9.01


H_0 = [
    r,  # r
    0,  # phi
    0,  # p_r
    p_phi,  # p_phi
]

T = np.linspace(0, 8571, 85710)


def H(H, t):
    r, phi, p_r, p_phi = H
    drdt = (1 - 2 / r) * p_r
    dphidt = p_phi / (r ** 2)
    dp_rdt = -(p_r ** 2) / (r ** 2) + (p_phi ** 2) / (r ** 3) - 1 / ((r - 2) ** 2)
    dp_phidt = 0
    dHdt = [drdt, dphidt, dp_rdt, dp_phidt]
    return dHdt


sol = odeint(H, H_0, T)

x = []

for i in sol:
    res = i[1] - arccos(r / i[0])
    x.append(res)


print(sol[85709][1])
plt.plot(sol)
plt.title('Near a black hole')
plt.xlabel('Time')
plt.ylabel('phi-arccos(r_{init}/r)')
plt.show()
