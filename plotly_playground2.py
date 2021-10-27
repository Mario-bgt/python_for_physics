import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced angles between 0 and pi/3
x = np.linspace(0, np.pi/3, 500)
x2 = [0, np.pi*10/180, np.pi*20/180, np.pi*30/180, np.pi*40/180, np.pi*50/180, np.pi*60/180, np.pi/3]

m = 2.5
n = 0.6
g = 9.81

# def y
y = (m*g*n)/(np.cos(x))
y2 = (m*g*n)/(np.cos(x2))

# def x ticks as angles in radians
tickx = [0, np.pi*10/180, np.pi*20/180, np.pi*30/180, np.pi*40/180, np.pi*50/180, np.pi*60/180, np.pi/3]
ticky = y2

# setting the axes at the centre
fig = plt.figure()

plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x2, y2, 'ro')
plt.ylabel('Kraft')
plt.xlabel('Winkel')
plt.title('F(α) = (m*g*n)/(cos(α)) zwischen 0° und 60°')
plt.tick_params(bottom=False, left=False)
plt.xticks(tickx)
plt.yticks(ticky)
plt.legend(loc='lower right')
plt.savefig('hw_3_2.pdf')
plt.show()
