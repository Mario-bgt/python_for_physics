import numpy as np
import matplotlib.pyplot as plt

Nx = 301
Nt = 100000
dx = 1 / (Nx - 1)
dt = 1e-7
x = np.linspace(0, 1, Nx)
psi0 = np.sqrt(2) * np.sin(np.pi * x)
mu, sigma = 1 / 2, 1 / 20
V = -1e4 * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
print(dt / dx ** 2)
plt.figure(figsize=(8, 3))
plt.plot(x, V)
plt.xlabel('$x$')
plt.ylabel('$V(x)$')
plt.show()
psi = np.zeros([Nt, Nx])
psi[0] = psi0
print(psi)


def compute_psi(psi):
    for t in range(0, Nt - 1):
        for i in range(1, Nx - 1):
            psi[t + 1][i] = psi[t][i] + 1j / 2 * dt / dx ** 2 * (
                    psi[t][i + 1] - 2 * psi[t][i] + psi[t][i - 1]) - 1j * dt * V[i] * psi[t][i]
        normal = np.sum(np.absolute(psi[t + 1]) ** 2) * dx
        for i in range(1, Nx - 1):
            psi[t + 1][i] = psi[t + 1][i] / normal
    return psi


psi_m1 = compute_psi(psi.astype(complex))
print(psi_m1)
print(np.absolute(psi_m1[5000]) ** 2)
print(x)
for i in range(len(psi_m1)):
    plt.plot(x, np.absolute(psi_m1[i]))
    plt.pause(0.1)
    plt.clf()
plt.show()
