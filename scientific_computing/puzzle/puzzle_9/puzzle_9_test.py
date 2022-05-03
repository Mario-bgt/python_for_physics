import numpy as np
import matplotlib.pyplot as plt

g = 10  # gravitational acceleration
L = 0.03  # radius of the wheel
l = 0.4  # length of pendulum
ohm = 10  # angular speed of the wheel
phi = [-np.pi / 4]  # angle of pendulum
omega = np.sqrt(g / l)  # natural frequency of the pendulum
tau = [0]  # location of the wheel
lama = L/l
gamma = (omega**2)/(ohm**2)
g = 9.81

v_phi = [0]
v_tau=[0]
tau_max = 300


def a(phi, tau):
    return -gamma * np.sin(phi) - lama * np.sin(phi - tau)

def v(phi, tau):
    return 0


dtau = 0.1

while tau[-1] < tau_max - dtau / 2:
    dphi = v_phi[-1] * dtau
    dv_phi = a(phi[-1], tau[-1]) * dtau
    tau.append(tau[-1] + dtau)
    phi.append(phi[-1] + dv_phi)

print(tau)
print(phi)
mp_x = L*np.sin(tau)
mp_y = -L*np.cos(tau)

pm_x = L*np.sin(tau) + l*np.sin(phi)
pm_y = -L*np.cos(tau)-l*np.cos(phi)

fig = plt.figure()

for t in range(1, len(tau)):
    x1 = pm_x[:t]
    y1 = pm_y[:t]
    x2 = mp_x[:t]
    y2 = mp_y[:t]
    plt.gca().clear()
    plt.plot(0, 0, 'yo')
    plt.plot(x2,y2)
    plt.plot(mp_x[t - 1:t], mp_y[t - 1:t], 'ro')
    plt.plot(x1, y1)
    plt.plot(pm_x[t - 1:t], pm_y[t - 1:t], 'ro')
    plt.plot([mp_x[t - 1:t],pm_x[t - 1:t]], [mp_y[t - 1:t],pm_y[t - 1:t]])
    plt.title('Both functions in one at ' + str(t / 10) + ' but more fancy')
    plt.pause(0.001)
plt.show()