import matplotlib.pyplot as plt
import numpy as np

# 500 linearly spaced angles between 0 and pi/3
x = np.linspace(0, np.pi/3, 500)
x2 = [0, np.pi*10/180, np.pi*20/180, np.pi*30/180, np.pi*40/180, np.pi*50/180, np.pi*60/180, np.pi/3]

#def mass, friction coefficient and g
m = 2.5
n = 0.6
g = 9.81

# def y
y = (m*g*n)/(np.cos(x)+np.sin(x)*n)
y2 = (m*g*n)/(np.cos(x2)+np.sin(x2)*n)

# def x ticks as angles in radians
tickx = [0, np.pi*10/180, np.pi*20/180, np.pi*30/180, np.pi*40/180, np.pi*50/180, np.pi*60/180, np.pi/3]
ticky = y2

# setting the axes at the centre
fig = plt.figure()

#plot line from x ans y
plt.plot(x, y, linewidth=0.5, color="black")
#plot every 10 degrees
plt.plot(x2, y2, 'ro')
#name y ax
plt.ylabel('Kraft')
#name x ax
plt.xlabel('Winkel')
#set title
plt.title('F(α) = (m*g*n)/(cos(α)+sin(α)*n) zwischen 0° und 60°')
#Change the appearance of ticks, tick labels, and gridlines
plt.tick_params(bottom=False, left=False)
#set xticks every 10 degrees
plt.xticks(tickx)
#set yticks to results of every 10 degree
plt.yticks(ticky)
#put legend in lower right pos
plt.legend(loc='lower right')
#safe plot as pdf
plt.savefig('hw_3.pdf')
#show plot in window
plt.show()
