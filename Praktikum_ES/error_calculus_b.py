import numpy as np

"""For calculating the medium value for x_0"""
values = [318,
          312.6,
          314.4,
          323.4,
          302.4,
          277.8,
          343.8,
          344.4,
          286.2
          ]
y = int(len(values))
x = 0

for i in values:
    x += i
x = (x / y)
print('The medium value for x_0 is: '+str(x))

"""For calculating the error upon x_0"""
error = 0
for i in values:
    error += (i - x)**2
error = np.sqrt((1 / (y * (y - 1))) * error)
print('The error upon x_0 is+-: ' + str(error))
