import numpy as np
from fractions import Fraction
from pi import *
import time
start = time.time()


def tann(tan_1, tan_2, n):
    if n == 1:
        return (tan_1+tan_2)/(1-tan_1*tan_2)
    x1 = n//2
    x2 = n-x1

    return (tan_1+tan_2)/(1-tan_1*tan_2)


