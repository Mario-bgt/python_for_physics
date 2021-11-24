import numpy as np

"""For calculating the medium value for x_0"""
values = [16.8,
          16.6,
          16.4,
          16.4,
          15.9, ]
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

"""For calculating the expected value for x_0"""
k = 23/30
y_s = 22.2
y_r = 10.5
x_0 = np.sqrt((2/k)*y_r*(y_s - y_r))
print('The expected value for x_0 is: ' + str(x_0))

"""For calculating the velocity"""
g = 9.81
t = np.sqrt((2 * y_r) / g)
v_1 = x / t
print('The value for v_1 should be: ' + str(v_1))
