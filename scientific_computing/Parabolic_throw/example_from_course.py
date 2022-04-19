""" wurf1d.py -- numerically calculate the position of an object thrown vertically

This minimal example uses the Euler method.
"""
import matplotlib.pyplot as plt

g = 9.81

t = [0]
y = [0]
v_y = [10]
t_max = 3


def a(y, t):
    """the derivative function"""
    return -g


dt = 0.01

while t[-1] < t_max - dt / 2:
    dy = v_y[-1] * dt
    dv_y = a(y[-1], t[-1]) * dt
    t.append(t[-1] + dt)
    y.append(y[-1] + dy)
    v_y.append(v_y[-1] + dv_y)

print(t)
print(y)
print(v_y)
fig, ax = plt.subplots(1, 1)
ax.plot(y, "bo", label=f"dt = {dt}")
ax.set_xlabel("step")
ax.set_ylabel("y position")
ax.set_title(f"Starting values: $y = {y[0]} m$, $v_y = {v_y[0]} m/s$")
ax.legend()
plt.show()