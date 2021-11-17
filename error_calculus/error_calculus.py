import numpy as np

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
x = 313.6666667


error = 0
for i in values:
    error += (i-x)**2

print(error)
error = np.sqrt(error/42)
print(error)
