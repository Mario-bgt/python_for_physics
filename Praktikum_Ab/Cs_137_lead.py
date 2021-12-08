import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
plt.figure(figsize = (6.69, 5.017500000000001))
y = [716,
     473,
     264,
     169,
     102,
     53,
     29,
     19,
     19,
     3,
     1,
     ]
yerr = [27.15,
        22.23,
        16.89,
        13.8,
        11.11,
        8.62,
        7.09,
        6.35,
        6.35,
        4.28,
        4.51,

        ]

x = np.linspace(0, 10, 11)

plt.grid(True, which="both")

# plt.semilogy(x, y, 'k', linewidth=0.5, linestyle='--', label=r'$f(\varphi_2)=\sin^{-1}\left(\frac{z_0}{2r}\right)$')
plt.errorbar(x=x, y=y, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=0.5, capsize=1, color="black",
             label=r'$N(x)\:measured$')
p = np.polyfit(x, np.log(y), 1)
plt.semilogy(x, np.exp(p[0] * x + p[1]), 'r--', linewidth=0.2, label=r'$f(x) = $' + str(p[0]) + 'x +' + str(p[1]))
slope = p[0]
# plt.ylim([1, 3000])
plt.xlim([-1, 11])
plt.title('source: Cs-137, slab-material: lead')
plt.xlabel(r'$amount\:of\:slabs$')
plt.ylabel(r'$N(x)$')
plt.legend(loc='upper right')
plt.savefig('Figure_3.pdf')
plt.show()
