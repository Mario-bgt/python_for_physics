import numpy as np
import matplotlib.pyplot as plt

N = 5
c = 299792458
G = 6.67428e-11
M = np.zeros(shape=(N, 1))
R = np.zeros(shape=(N, 2))
V = 0 * R
A = 0 * R
data = np.loadtxt('data.txt')
P_x = []
P_y = []

j = 0
for i in data:
    M[j] = i[0]
    R[j] = [i[1], i[2]]
    V[j] = [i[3], i[4]]
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


t_max = 36000*24*2
dt = 300
time = 0

while time < t_max:
    for j in range(5):
        a_x = 0
        a_y = 0
        for i in range(5):
            if j != i:
                a_x += (M[j]*(R[i][0]-R[j][0]))/(abs(R[i][0]-R[j][0])**3)
                a_y += (M[j]*(R[i][1]-R[j][1]))/(abs(R[i][1]-R[j][1])**3)
        A[j] = [-G*a_x, -G*a_y]
    V = V + A*dt
    R = R + V*dt/2
    for i in R:
        x = i[0]
        y = i[1]
        P_x.append(x)
        P_y.append(y)
    time = time + dt


for i in range(int(len(P_x)/5)):
    plt.xlim([min(P_x), max(P_x)])
    plt.ylim([min(P_y), max(P_y)])
    for j in range(5):
        plt.plot(P_x[i+j], P_y[i+j],'bo', markersize=2)
    plt.title('Zeit in Stunden: ' + str(i*5*1800/3600))
    plt.pause(0.1)
    plt.clf()


plt.show()




