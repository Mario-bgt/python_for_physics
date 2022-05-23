import numpy as np

x = np.asarray([5, 6, 6, 7, 9, 7, 2, 2])


def G_four(x):
    if len(x) == 1:
        return x
    N = len(x)
    x_even = x[::2]
    x_odd = x[1::2]
    print(x_even, type(x_even))
    omega_N = np.exp(-2j * np.pi/N)
    print(omega_N, type(omega_N))
    a_p = []
    s_p = []
    for i in range(N // 2):
        a_p.append(G_four(x_even) + (omega_N**i)*G_four(x_odd))
        s_p.append(G_four(x_even) - (omega_N**i)*G_four(x_odd))
    return [a_p, s_p]


print(G_four(np.array([5, 6, 6, 7, 9, 7, 2, 2])))
