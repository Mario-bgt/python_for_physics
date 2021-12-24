import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()


x = np.linspace(2, 200001, 200000)
y = 1/(np.log(x)**np.log(x))

sum = 0
suml = []
for i in y:
    sum += i
    suml.append(sum)


print(sum)

#plt.plot(x, y, '.k', linewidth=0.5, )
plt.plot(x, suml, '.r', linewidth=0.5, )
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='upper left')
plt.show()
