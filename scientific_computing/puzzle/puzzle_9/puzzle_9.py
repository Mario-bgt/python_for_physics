import numpy as np
import matplotlib.pyplot as plt

g = 10  # gravitational acceleration
L = 0.03  # radius of the wheel
l = 0.4  # length of pendulum
ohm = 10  # angular speed of the wheel
phi = [-np.pi / 4]  # angle of pendulum
omega = np.sqrt(g / l)  # natural frequency of the pendulum
tau = [0]  # location of the wheel
lamba = 0.075
varphi = 0.25


"""
The center of the wheel is at (0,0)

The mounting point is at (L*sin(tau,-L*cos(tau)

The mass of the pendulum is at:
(L*sin(tau)+l*sin(phi), -L*cos(tau)-l*cos(phi))

Set ax length fixd to \pm (L+l)
"""

def acc(phi2, tau2):
    -varphi*np.sin(phi2)