import matplotlib.pyplot as plt

g = 9.81

t = [0]
y = [0]
x = [0]
v_y = [14]
v_x = [15]
t_max = 3.2


def a(y, t):
    return -g

def a2(x, t):
    return 0

dt = 0.0001

while t[-1] < t_max - dt / 2:
    dy = v_y[-1] * dt
    dx = v_x[-1] * dt
    dv_y = a(y[-1], t[-1]) * dt
    dv_x = a2(x[-1], t[-1]) * dt
    t.append(t[-1] + dt)
    y.append(y[-1] + dy)
    x.append(x[-1] + dx)
    v_y.append(v_y[-1] + dv_y)
    v_x.append(v_x[-1] + dv_x)

print(x[-1])
print(y[-1])
fig = plt.figure()
plt.plot(x, y)
plt.show()