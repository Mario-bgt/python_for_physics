import numpy as np

"""For calculating the medium value for x_0"""
values = [23.9,
          24.5,
          24.55696203,
          24.92857143,
          24.83333333,
          26.1,
          26.26506024,
          28.03571429,
          30,
          35
          ]

y = int(len(values))
x = 0

for i in values:
    x += i
x = (x / y)
print('The medium value for x_0 is: ' + str(x))

"""For calculating the error upon x_0"""
error = 0
for i in values:
    error += (i - x) ** 2
error = np.sqrt((1 / (y * (y - 1))) * error)
print('The error upon x_0 is+-: ' + str(error))
