""" wurf2d_odeint.py -- numerically calculate the position of an object in a parabolic throw

This example uses scipy.integrate.odeint
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.81

Y_0 = [
        0,   # x
        0,   # y
        5,   # v_x
        15,  # v_y
]
T = np.linspace(0,3,30)

def throw(Y,t):
    """ calculate the change for each component of Y """
    x,y,v_x,v_y = Y
    dxdt = v_x
    dydt = v_y
    dv_xdt = 0
    dv_ydt = -g
    dYdt = [dxdt, dydt, dv_xdt, dv_ydt]
    return dYdt

sol = odeint(throw, Y_0, T)

plt.plot(sol[:, 0], sol[:,1],'bo')
plt.plot(Y_0[2]*T,Y_0[3]*T-0.5*g*T**2, 'g')
plt.show()
