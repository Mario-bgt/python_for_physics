# puzzle 10
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("gliese.txt")

time = 0
tmax = 3600 * 24 * 2
dt = 600


# function for velocity
# we take the previous velocity and add dv
def dr(lis, i, a):
    v = lis[i][-1] + dt * a
    return v


# derivative of velocity
# dat is the data file, lis is either xdat or ydat
# this only works for one direction
def bes(dat, lis, k):
    a = 0
    for l in range(0, 5):
        if l != k:
            a = a + (m[l] * ((lis[k][-1] - lis[l][-1]) / (np.linalg.norm(lis[k][-1] - lis[l][-1]) ** 3)))
    return -a


# list for mass
m = []
# list of lists for x,y pos
xdat = [[], [], [], [], []]
ydat = [[], [], [], [], []]
# list for velocities
vxdat = [[], [], [], [], []]
vydat = [[], [], [], [], []]

# entering beginning values
for i in range(5):
    m.append(data[i][0])
    xdat[i].append(data[i][1])
    ydat[i].append(data[i][2])
    vxdat[i].append(data[i][3])
    vydat[i].append(data[i][4])

print(data)
print(xdat)
print(m)
print(vydat)
# calculating orbits
while time < tmax:
    #     plt.clf()
    #     plt.xlim((-200,200))
    #     plt.ylim((-150,150))
    for i in range(5):
        drx = (xdat[i][-1] + vxdat[i][-1] * dt) / 2
        dry = (ydat[i][-1] + vydat[i][-1] * dt) / 2

        dvx = bes(data, xdat, i)
        dvy = bes(data, ydat, i)

        vxdat[i].append(vxdat[i][-1] + dvx * dt)
        vydat[i].append(vxdat[i][-1] + dvy * dt)

        drx = (drx + vxdat[i][-1] * dt) / 2
        dry = (dry + vydat[i][-1] * dt) / 2

        xdat[i].append(xdat[i][-1] + drx)
        ydat[i].append(xdat[i][-1] + dry)

    time = time + dt

print(xdat)
for i in range(len(xdat)):
    for j in range(5):
        plt.plot(xdat[j][i], ydat[j][i], 'yo', markersize=1)
    plt.pause(0.01)
    plt.gcf()

# plt.plot(xdat,ydat)
plt.show()
