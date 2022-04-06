import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt


g = 9.81
m_g = 0.015
m_p = 18
a = 0.13962634015955
l = 1.2

x = np.linspace(0, np.pi)
y = 2*np.sqrt(g*l)*np.sin(x/2)*(m_g+m_p)/m_g


fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black", label=r'$V_g(\alpha)=2\cdot  \sqrt{g\cdot l}\cdot\sin( \frac{\alpha}{2})\cdot  \frac{m_g + m_p }{m_g} $')
plt.tick_params(bottom=False, left=False)
plt.title(r'$Aufgabe\:1$')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$V_g$')
plt.legend(loc='lower right')
plt.savefig('s1.pdf')
plt.show()
