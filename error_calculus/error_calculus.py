import numpy as np

values = [3.3*10**(-5),
          2.97*10**(-5),
          2.805*10**(-5),
          3.3*10**(-5),
          2.97*10**(-5),
          2.805*10**(-5),
          2.805*10**(-5),
          3.3*10**(-5),
          2.805*10**(-5),
          3.006666667*10**(-5)
          ]
summe = 0
n = len(values)
for i in values:
    summe += i
mittelwert = summe/n
print('Der Mittelwert beträgt:', mittelwert)

error = 0
for i in values:
    error += (i - mittelwert) ** 2

error = np.sqrt(error / (n * (n - 1)))
print('Der statistische fehler beträgt:', error)
