import numpy as np
import matplotlib.pyplot as plt

N = 5
A = np.zeros((N, 2))
data = np.loadtxt('data.txt')
M = data[:, 0]
R = data[:, 1:3]
V = data[:, 3:5]
P_x = []
P_y = []


def kin():
    kinetic = 0
    for r in range(N):
        kinetic = kinetic + M[k] * np.sum(V[k] * V[k]) / 2
    return kinetic


def pot():
    potentiel = 0
    for s in range(N):
        for t in range(s):
            dR = R[s] - R[t]
            distance = np.linalg.norm(dR)
            potentiel = potentiel - M[s] * M[t] / distance
    return potentiel


t_max = 288000 * 24 * 2
dt = 600
time = 0
E_tot = []
while time < t_max:
    R = R + V * dt / 2
    for k in range(5):
        a_k = [0, 0]
        for l in range(5):
            if l != k:
                a_k += (M[l] * (R[k] - R[l])) / (np.linalg.norm(R[k] - R[l]) ** 3)
        A[k] = -1 * a_k
    V = V + A * dt
    R = R + V * dt / 2
    E_tot.append(kin() + pot())
    P_x.append(R[:, 0])
    P_y.append(R[:, 1])
    time = time + dt

P_x_f = np.array(P_x)
P_y_f = np.array(P_y)
fig, ax = plt.subplots()

img = plt.imread('img.jpg')
ax.imshow(img, extent=[-200, 200, -200, 200])
plt.plot(P_x_f, P_y_f)
plt.show()
for i in range(len(P_x)):
    plt.plot(P_x_f[i*5], P_y_f[i*5], 'y.', markersize=1)
    plt.ylim(-200, 200)
    plt.xlim(-200, 200)
    plt.pause(0.01)
