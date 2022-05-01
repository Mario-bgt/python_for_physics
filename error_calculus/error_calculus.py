import numpy as np

values = [1.62,1.56,1.59,1.56,1.49,1.5]
x = 1.55

error = 0
for i in values:
    error += (i - x)**2

n = len(values)
error = np.sqrt(error /(n*(n-1)))
print(error)
