import numpy as np
import matplotlib.pyplot as plt

N = 5
c = 299792458
G = 6.67428e-11
M = N * [0]
R = np.zeros(shape=(N, 2))
V = 0 * R
A = 0 * R
data = np.loadtxt('data.txt')
P_x = []
P_y = []

j = 0
for i in data:
    M[j] = (i[0]*c**3)/G
    R[j] = [i[1]*c, i[2]*c]
    V[j] = [c-i[3], c-i[4]]
    j += 1

R_tot = R


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
time = 0

while time < t_max:
    for j in range(5):
        a_x = 0
        a_y = 0
        for i in range(5):
            if j != i:
                a_x += (M[i]*(R[j][0]-R[i][0]))/(abs(R[j][0]-R[i][0])**3)
                a_y += (M[i]*(R[j][1]-R[i][1]))/(abs(R[j][1]-R[i][1])**3)
        A[j] = [-G*a_x, -G*a_y]
    V[j] = A[j]*dt
    R[j] = V[j]*dt/2
    time = time + dt
    plt.xlim([-8560617435.081961, 35241756353.320004])
    plt.ylim([-301629138332.50128, 7836989936.12])
    plt.plot(R, 'bo')
    plt.pause(1)
    plt.clf()
plt.show()
