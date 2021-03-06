import numpy as np
from fractions import Fraction
from pi import *
import time
start = time.time()


def tanplus(tan_1, tan_2):
    return (tan_1+tan_2)/(1-tan_1*tan_2)


tan_alpha = Fraction(1, 8)
N = 4
tan_Nalpha = tan_alpha
for i in range(int(N/2)):
    tan_Nalpha = tanplus(tan_Nalpha, tan_Nalpha)

tan_beta = tanplus(1, -1*tan_Nalpha)
print(N, tan_alpha, tan_beta)
print(frac_to_string(4*(N*arctan(tan_alpha)+arctan(tan_beta))))
end = time.time()
print('It took', (end - start), 'seconds to execute.')

#2 1/5 7/17 works
#4 1/8 1697/5729
''''def tann(tan_1, tan_2, n):
    if n == 1:
        return (tan_1+tan_2)/(1-tan_1*tan_2)
    x1 = n//2
    x2 = n-x1
    return


tan_alpha = Fraction(1, 8)
tan_Nalpha = tann(tan_alpha, tan_alpha, 5)
tan_beta = tann(1, -1*tan_Nalpha, 2)

print(tan_beta)'''