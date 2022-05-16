import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

y = [49.4, 49.30, 49.10, 49.00, 48.90, 48.70, 48.70, 48.50, 48.40, 48.30, 48.20, 17.50, 16.90, 16.00, 16.30, 15.50,
     14.90, 13.50, 12.50, 11.90, 11.50, 11.50, 11.50, 11.50, 11.50, 11.50]

x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 305, 310, 315, 320, 325, 330, 360, 390, 420, 450, 480, 510, 540,
     570, 600]

fig = plt.figure()
plt.plot(x, y, 'ko', markersize=3, color="black", label=r'$Data\:points$')
plt.plot(x, y, linewidth='0.5', linestyle='dashed', color='black')
plt.plot([0, 300], [48.2, 48.2], linewidth='1', linestyle='dashed', color='red', label=r'$T_1$')
plt.plot([390, 600], [11.9, 11.9], linewidth='1', linestyle='dashed', color='blue', label=r'$T_G$')
plt.ylabel(r'$Temperature\:in\:[C]$')
plt.xlabel(r'$Time\:in\:[s]$')
plt.title(r'$Temperature\:plottet\:agains\:time$')
plt.legend(loc='best')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.savefig('graph2.pdf')
plt.show()
