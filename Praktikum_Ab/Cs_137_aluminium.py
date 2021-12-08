import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

plt.figure(figsize = (6.69, 5.017500000000001))
y = [716,
     492,
     344,
     203,
     141,
     74,
     ]
yerr = [27.15,
        22.66,
        19.11,
        14.98,
        12.74,
        9.76,
        ]

x = np.linspace(0, 5, 6)

plt.grid(True, which="both")

# plt.semilogy(x, y, 'k', linewidth=0.5, linestyle='--', label=r'$f(\varphi_2)=\sin^{-1}\left(\frac{z_0}{2r}\right)$')
plt.errorbar(x=x, y=y, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=0.5, capsize=1, color="black",
             label=r'$N(x)\:measured$')
p = np.polyfit(x, np.log(y), 1)
plt.semilogy(x, np.exp(p[0] * x + p[1]), 'r--', linewidth=0.2, label=r'$f(x) = $' + str(p[0]) + 'x +' + str(p[1]))
slope = p[0]
# plt.ylim([1, 3000])
plt.xlim([-1, 6])
plt.title('source: Cs-137, slab-material: aluminium')
plt.xlabel(r'$amount\:of\:slabs$')
plt.ylabel(r'$N(x)$')
plt.legend(loc='upper right')

plt.savefig('Figure_4.pdf')
plt.show()
