import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [0.323101777, 0.412031314, 0.484730974, 0.513874615, 0.536193029,
     0.556792873, 0.577034045, 0.596658711, 0.650618087, 0.673854447]
y = np.array([1, 1.4, 3.4, 7.2, 13.1, 5.8, 3.5, 1.9, 1.2, 0.8])
z = np.array([6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, ])
"""
dt = np.array([
    [0.323101777, 0.8],
    [0.412031314, 1.2],
    [0.484730974, 5],
    [0.513874615, 8.2],
    [0.536193029, 16],
    [0.556792873, 7],
    [0.577034045, 4.5],
    [0.596658711, 2],
    [0.650618087, 1.1],
    [0.673854447, 0.8]

])"""

plt.plot(x, y, 'kx', markersize=5, color="black")
plt.plot(x, y, 'k', linewidth=0.2, linestyle='--')
plt.plot(x, z, 'k', linewidth=0.5)
plt.ylabel(r'$A(\omega)$')
plt.xlabel(r'$\omega$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph_4.pdf')
plt.show()
