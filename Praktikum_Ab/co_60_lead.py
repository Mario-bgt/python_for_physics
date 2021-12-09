import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

plt.figure(figsize = (6.69, 5.017500000000001))

y = [2151,
     1630,
     1239,
     931,
     757,
     563,
     409,
     328,
     276,
     202,
     166,

     ]
yerr = [46.61,
        40.64,
        35.5,
        30.86,
        27.9,
        24.17,
        20.74,
        18.69,
        17.24,
        14.94,
        13.69,

        ]

x = np.linspace(0, 10, 11)


plt.grid(True, which="both")

#plt.semilogy(x, y, 'k', linewidth=0.5, linestyle='--', label=r'$f(\varphi_2)=\sin^{-1}\left(\frac{z_0}{2r}\right)$')
plt.errorbar(x=x, y=y, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=0.5, capsize=1, color="black",label=r'$N(x)\:measured$')
p = np.polyfit(x, np.log(y), 1)
plt.semilogy(x, np.exp(p[0] * x + p[1]), 'r--', linewidth=0.2, label=r'$f(x) = $'+str(p[0])+'x +'+str(p[1]))
slope = p[0]
#plt.ylim([1, 3000])
plt.xlim([-1, 11])
plt.title('source: Co-60, slab-material: lead')
plt.xlabel(r'$amount\:of\:slabs$')
plt.ylabel(r'$N(x)$')
plt.legend(loc='upper right')
plt.savefig('Figure_1.pdf')
plt.show()
