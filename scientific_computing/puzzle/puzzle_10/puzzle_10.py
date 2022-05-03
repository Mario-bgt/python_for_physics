import numpy as np
import matplotlib.pyplot as plt

N = 5
c = 299792458
G = 6.67428e-11
M = N * [0]
R = np.zeros(shape=(N, 2))
V = 0 * R
data = np.loadtxt('data.txt')

j = 0
for i in data:
    M[j] = i[0]*c/G
    R[j] = [i[1]*c, i[2]*c]
    V[j] = [i[3]*c, i[4]*c]
    j += 1


def kin(kin):
    for k in range(N):
        kin = kin + M[k] * np.sum(V[k] * V[k]) / 2
    return kin


def pot(pot):
    for k in range(N):
        for l in range(k):
            dR = R[k] - R[l]
            distance = np.linalg.norm(dR)
            pot = pot - M[k] * M[l] / distance
    return pot


t_max = 3600*24*2
dt = 1800

fig = plt.figure()

for j in range(5):
    plt.plot(R[j][0], R[j][1], 'ro')
plt.show()

print(M)
print(R)
print(V)
