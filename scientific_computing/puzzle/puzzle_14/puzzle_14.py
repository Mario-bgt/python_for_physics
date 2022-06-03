import numpy as np
from fractions import Fraction
from pi import *


def tann(tan_1, tan_2, n, check=2):
    tan_new = (tan_1 + tan_2) / (1 - tan_1 * tan_2)
    if check >= n:
        return tan_new
    if check < n:
        check += 1
        return tann(tan_new, tan_2, n, check)


N = 8
a = 4
tan_alpha = Fraction(1, a)
tan_Nalpha = tann(tan_alpha, tan_alpha, N)
tan_beta = (1 - tan_Nalpha) / (1 + tan_Nalpha)
print(N, tan_alpha, tan_beta)
print(4 * (N * np.arctan(float(tan_alpha)) + np.arctan(float(tan_beta))))
