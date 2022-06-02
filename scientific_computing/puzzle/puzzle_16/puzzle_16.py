import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as npf

plt.style.use('dark_background')


def V(x):
    return (1 / 2) * x ** 2


def psi_0(x):
    return np.pi ** (-1 / 4) * np.exp(-x ** 2 / 2)


def psi_n(x, n):
    if n == 1:
        return psi_0(x)
    if n == 2:
        return np.sqrt(2 / n) * x * psi_0(x)
    return np.sqrt(2 / n) * x * psi_n(x, n - 1) - np.sqrt((n - 1) / n) * psi_n(x, n - 2)


N = 2 ** 9
dt = 0.1
dx = (2 * np.pi / N) ** .5
x = (np.arange(N) - N // 2) * dx
dk = (2 * np.pi) / (N * dx)
k = (np.arange(N) - N // 2) * dk
function = psi_n(x, 2)
plt.plot(function)
plt.show()
while True:
    fft = np.fft.fftshift(np.fft.fft(np.fft.fftshift(function)))
    fft = fft * np.exp(-1j * k ** 2 * (dt / 2))
    ift = np.fft.fftshift(np.fft.ifft(np.fft.fftshift(fft)))
    ift = ift * np.exp(-1j * V(x) * dt)
    fft = np.fft.fftshift(np.fft.fft(np.fft.fftshift(ift)))
    fft = fft * np.exp(-1j * k ** 2 * (dt / 2))
    function = np.fft.fftshift(np.fft.ifft(np.fft.fftshift(fft)))
    real = []
    imag = []
    prob = []
    for i in function:
        real.append(i.real)
        imag.append(i.imag)
        prob.append(np.abs(i) ** 2)
    plt.ylim(-1, 1)
    plt.plot(prob)
    plt.plot(real)
    plt.plot(imag)
    plt.pause(0.01)
    plt.gca().clear()
