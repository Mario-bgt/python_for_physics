import numpy as np
import matplotlib.pyplot as plt

lam = 0.075
varphi = 0.25

tau = [0]
phi = [0]
v_y = [10]
t_max = 3


def a(phi, tau):
    """the derivative function"""
    return -varphi*np.sin(phi)-lam*np.sin(phi-tau)


dt = 0.1
# `t_max - dt/2` to ensure t[-1] = 2.999999 still terminates the loop
while tau[-1] < t_max - dt / 2:
    dy = v_y[-1] * dt
    dv_y = a(phi[-1], tau[-1]) * dt
    tau.append(tau[-1] + dt)
    phi.append(phi[-1] + dy)
    v_y.append(v_y[-1] + dv_y)

print(phi)
print(tau)
print(v_y)