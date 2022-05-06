import numpy as np


y = [11.53, 10.97, 10.23, 9.33, 8, 6.18, 4.26, 2.16, 0.14]
yerr =[]
for i in y:
    err = np.sqrt((i*0.015)**2+(i*0.0025)**2)
    yerr.append(err)

for i in range(8):
    print(y[i],yerr[i])