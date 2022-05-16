import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

y = [50.4, 50.2, 49.9, 49.9, 49.7, 49.5, 49.4, 49.2, 49.1, 49, 33, 33, 32.9, 32.9, 32.9, 32.9, 32.9, 32.7, 32.7, 32.7,
     32.7]

x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]

fig = plt.figure()
plt.plot(x, y, 'ko', markersize=3, color="black", label=r'$Data\:points$')
plt.plot(x, y, linewidth='0.5', linestyle='dashed', color='black')
plt.plot([0, 270], [49, 49], linewidth='1', linestyle='dashed', color='red', label=r'$T_A$')
plt.plot([300, 600], [33, 33], linewidth='1', linestyle='dashed', color='blue', label=r'$T_G$')
plt.ylabel(r'$Temperature\:in\:[C]$')
plt.xlabel(r'$Time\:in\:[s]$')
plt.title(r'$Temperature\:plottet\:agains\:time$')
plt.legend(loc='best')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph.pdf')
plt.show()
