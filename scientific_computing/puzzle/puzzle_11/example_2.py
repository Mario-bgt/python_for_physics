""" wurf2d_odeint.py -- numerically calculate the position of an object in a parabolic throw

This example uses scipy.integrate.solve_ivp
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

g = 9.81

Y_0 = [
        0,   # x
        0,   # y
        5,   # v_x
        15,  # v_y
]
T = np.linspace(0,3,30)
T_span = T[0], T[-1]

def throw(t,Y):      # note: ordering of arguments swapped w.r.t odeint
    """ calculate the change for each component Y """
    x,y,v_x,v_y = Y
    dxdt = v_x
    dydt = v_y
    dv_xdt = 0
    dv_ydt = -g
    dYdt = [dxdt, dydt, dv_xdt, dv_ydt]
    return dYdt

sol = solve_ivp(throw, T_span, Y_0, t_eval=T)
# note: sol is an object with several attributes now
#       the values returned by odeint are in the sol.y data-attribute
print(np.all(T == sol.t))

plt.plot(sol.y[0],sol.y[1],'bo') # note: rows/cols swapped w.r.t odeint
plt.plot(Y_0[2]*T,Y_0[3]*T-0.5*g*T**2, 'g')
plt.show()
