import numpy as np
import matplotlib.pyplot as plt


def V(x):
    return (1/2)*x**2


def psi_0(x):
    return np.pi**(-1/4)*np.exp(-x**2/2)


def psi_n(x, n):
    if n == 1:
        return np.sqrt(2/n)*x*psi_0(x)
    return np.sqrt(2/n)*x*psi_n(x, n-1)-np.sqrt((n-1)/n)*psi_n(x, n-2)


N = 20
n = np.arange(N)-N/2
dt = 0.01
dx = 0.01
t_max = 300
x = np.linspace(-150, 150, 301)
t = 0
while t < t_max:
    psy_n = []
    for x_n in x:
        fft = np.fft.fft(n)
        k = (2*np.pi)/(N*dx)
        fft = fft*np.exp(-complex(0, 1)*k**2*(dt/2))
        ift = np.fft.ifft(fft)
        ift = ift*np.exp(-complex(0, 1)*V(x_n)*dt)
        fft = np.fft.fft(ift)
        fft = fft*np.exp(-complex(0, 1)*k**2*(dt/2))
        ift = np.fft.ifft(fft)
        real = []
        imag = []
        for i in ift:
            print(i, i.real, i.imag)
            real.append(i.real)
            imag.append(i.imag)
        plt.plot(real)
        plt.plot(imag)
        plt.pause(0.1)
    t += dt


