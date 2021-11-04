import matplotlib.pyplot as plt
import numpy as np

# mesurements time
x = [0.323101777, 0.412031314, 0.484730974,
     0.513874615, 0.536193029, 0.556792873,
     0.577034045, 0.596658711, 0.650618087,
     0.673854447]

# mesurements amplitude
y = [1, 1.4, 3.4, 7.2, 13.1, 4.6, 4, 1.9, 1.2, 0.6]
z = [6.55, 6.55, 6.55, 6.55, 6.55, 6.55, 6.55, 6.55, 6.55, 6.55,]


# setting the axes at the centre
fig = plt.figure()
plt.plot(x, y, linewidth=0.5, color="black")
plt.plot(x,z, linewidth=0.5, color="red")
plt.plot(x, y, 'ro')
plt.tick_params(bottom=False, left=False)
plt.title('with 0.4 amps')
plt.savefig('s6_a2_c.pdf')
print(y)
plt.show()
