import numpy as np
import matplotlib.pyplot as plt


def V(x):
    return (1/2)*x**2


N = 300
n = np.arange(N)-N/2
dt = 0.1
dx = 0.1
t_max = 300
x_max = 300
while dt < t_max:
    for x_n in range(x_max):
        fft = np.fft.fft(n)
        k = (2*np.pi)/(N*dx)
        fft = fft*np.exp(-complex(0, 1)*k**2*(dt/2))
        ift = np.fft.ifft(fft)
        ift = ift*np.exp(-complex(0, 1)*V(x_n)*dt)
        fft = np.fft.fft(ift)
        fft = fft*np.exp(-complex(0, 1)*k**2*(dt/2))
        ift = np.fft.ifft(fft)
    dt += dt


