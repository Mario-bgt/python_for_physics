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


N = 2**8
n = np.arange(N)-N/2
dt = 0.01
dx = (2*np.pi/N)**.5
t_max = 300
x = np.arange((N)-N//2) * dx
t = 0
k = (2 * np.pi) / (N * dx) * n
psy = psi_0(x)
#plt.plot(psy)
#plt.show()
#np.fft.fftshift(np.fft(np.fftshift()))
while t < t_max:
    fft = np.fft.fft(psy)
    fft = fft*np.exp(-1j*k**2*(dt/2))
    ift = np.fft.ifft(fft)
    for i, x_n in enumerate(x):
        ift[i] = ift[i]*np.exp(-1j*V(x_n)*dt)
    fft = np.fft.fft(ift)
    fft = fft*np.exp(-1j*k**2*(dt/2))
    psy = np.fft.ifft(fft)
    real = []
    imag = []
    prob = []
    for i in psy:
        print(i, i.real, i.imag)
        real.append(i.real)
        imag.append(i.imag)
        prob.append(np.abs(i)**2)
    plt.ylim(0,1)
    plt.plot(prob)
    #plt.plot(real)
    #plt.plot(imag)
    plt.pause(0.1)
    plt.gca().clear()
    t += dt


