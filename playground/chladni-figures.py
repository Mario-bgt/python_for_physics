from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

n = 1
m = 1
u = 1
w = 200*np.sqrt(n**2+m**2)
def V(x,y,z):
     return u*np.cos(w*z)*np.sin(((n*np.pi)/1)*x)*np.sin(((m*np.pi)/1)*y)

X,Y = np.mgrid[-1:1:100j, -1:1:100j]
Z_vals = [ 5, 0, 0.9 ]
num_subplots = len( Z_vals)

fig = plt.figure(figsize=(10, 4))
for i,z in enumerate( Z_vals):
    ax = fig.add_subplot(1 , num_subplots , i+1, projection='3d')
    ax.contour(X, Y, V(X,Y,z), cmap=cm.gnuplot)
    ax.set_title('z = %.2f'%z, fontsize=30)
plt.show()