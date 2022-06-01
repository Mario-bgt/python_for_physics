import numpy as np


def fouriertransformator(x):
    if len(x) == 1:
        return x
    N = len(x)
    lyst = np.arange(N//2)
    res = x*0
    x_even = x[::2]
    x_odd = x[1::2]
    omega_N = np.exp(-2j * np.pi*lyst/N)
    res[:N//2] = fouriertransformator(x_even) + omega_N * fouriertransformator(x_odd)
    res[N//2:] = fouriertransformator(x_even) - omega_N * fouriertransformator(x_odd)
    return res


x = [5, 6, 6, 7, 9, 7, 2, 2]
sol = fouriertransformator(x)
print(sol[-1])
print(np.fft.fft(x)[-1])
