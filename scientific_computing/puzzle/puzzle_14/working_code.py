import numpy as np
from fractions import Fraction
from pi import *
import time
start = time.time()


def tanplus(tan_1, tan_2):
    return (tan_1+tan_2)/(1-tan_1*tan_2)


tan_alpha = Fraction(1, 8)
N = 6
tan_2alpha = tanplus(tan_alpha, tan_alpha)
tan_4alpha = tanplus(tan_2alpha, tan_2alpha)
tan_6alpha = tanplus(tan_4alpha, tan_4alpha)
tan_beta = tanplus(1, -1*tan_4alpha)
print(N, tan_alpha, tan_beta)
end = time.time()
print('It took', (end - start), 'seconds to execute.')

#2 1/5 7/17 works
#4 1/8 1697/5729