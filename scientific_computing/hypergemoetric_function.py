import numpy as np
np.arctan()

def T_k(a, b, c, k):
    if k == 0:
        return 1
    else:
        return (a + (k - 1) * (b + (k - 1))) / ((c + (k - 1)) * k)


z = -0.234647
n = 1
summe = 1

while n < 40000:
    tk = T_k(1, 1, 2, n)*z*T_k(1, 1, 2, n-1)
    summe = summe + tk
    n += 1
    print(summe)
    if n == 40000:
        print(summe)
