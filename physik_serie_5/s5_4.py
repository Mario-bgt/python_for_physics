import matplotlib.pyplot as plt
import numpy as np

g = 10
m = 0.5
F = 25
w = (2*np.pi)/0.4
n = 1.2

y = []

t = np.linspace(0, 0.25, 1000)
for x in t:
    if x < 0.2:
        p = F * np.sin(w * x)
        y.append(p)
    else:
        y.append(0)


z = F*np.sin(w*t*0.8)*0.8
a = np.linspace(0, 0, 1000)

fig = plt.figure()
plt.plot(t, y, linewidth=0.5, color="black", label="default")
plt.plot(t, z, linewidth=0.5, color="red", label="modifiziert")
plt.tick_params(bottom=False, left=False)
plt.title('Kraftstoss Serie 4')
plt.xlabel('Zeit in Sekunden')
plt.legend(loc='upper right')
plt.savefig('s5_4.pdf')
print(z)
plt.show()


