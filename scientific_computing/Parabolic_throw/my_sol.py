import matplotlib.pyplot as plt
import numpy as np

v_y = 14
v_x = 15
g = 9.81


def pos(t):
    x = v_x*t
    y = v_y*t-0.5*g*t**2
    return x, y

print(pos(3.2))
