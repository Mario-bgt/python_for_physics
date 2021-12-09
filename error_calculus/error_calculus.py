import numpy as np

values = [10,
          9,
          8,
          12,
          11,
          17,
          15,
          15,
          12,
          7,
          6,
          13,
          11,
          8,
          10,
          11,
          10,
          9,
          10,
          13,
          10,
          10,
          6,
          9,
          14,
          5,
          18,
          4,
          8,
          8,
          8,
          13,
          6,
          3,
          13,
          10,
          10,
          12,
          12,
          9,
          13,
          15,
          14,
          13,
          11,
          18,
          8,
          6,
          16,
          10,
          ]
x = 10.58

error = 0
for i in values:
    error += (i - x)**2

n = len(values)
error = np.sqrt(error /(n*(n-1)))
print(error)
