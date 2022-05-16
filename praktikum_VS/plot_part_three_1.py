import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

x = [175000, 170000, 165000, 160000,
     155000, 150000, 145000, 140000, 135000, 130000, 125000, 120000, 115000, 110000]
y = [393.15, 392.15, 391.15, 390.65,
     389.15, 388.15, 387.15, 387.15, 385.65, 384.15, 383.15, 382.15, 381.15, 379.15]
yerr = 0.5
xerr = 2000

#plt.plot(x, y, 'ko', label=r'$f(\varphi_2)=\sin^{-1}\left(\frac{z_0}{2r}\right)$')
plt.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=0.5, capsize=1, color="black",
             label=r'$p_D(T)$')
plt.ylabel(r'$Tempreature\:in\:[K]$')
plt.xlabel(r'$Pressure\:in\:[Pa]$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.savefig('graph_3_1.pdf')
plt.show()
