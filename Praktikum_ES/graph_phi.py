import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()


x = np.linspace(-2,2,200)
y = np.arcsin(x/2)

plt.plot(x, y, 'k', linewidth=0.5, linestyle='--', label=r'$f(\varphi_2)=\sin^{-1}\left(\frac{z_0}{2r}\right)$')

plt.ylabel(r'$\varphi_2\:(rad)$')
plt.xlabel(r'$z_0\:(cm)$')
plt.title(r'$scattering\:angle\:\varphi_2\:as\:a\:function\:of\:the\:impact\:parameter\:z_0$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='upper left')
plt.savefig('graph_1.pdf')
plt.show()
