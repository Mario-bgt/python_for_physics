import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()

def solve_lineqs(A, b):
    wert, Vek = np.linalg.eigh(A)
    for i in range(len(wert)):
        if wert[i] < 1e-12:
            wert[i] = 0
        else:
            wert[i] = 1 / wert[i]
    Ainv = Vek @ np.diag(wert) @ Vek.T
    return Ainv @ b


def dd(x, y):
    return y * N + x


def neighbour(x, y):
    return (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)


N = 120
R = np.zeros((N ** 2, N ** 2))
np.fill_diagonal(R, 4)
b = np.zeros((N ** 2, 1))
b[0][0] = 1

for i in range(N):
    R[i * N][i * N + N - 1] = -1
    R[i * N + N - 1][i * N] = -1
    R[i][N ** 2 - N + i] = -1
    R[N ** 2 - N + i][i] = -1
    for j in range(N):
        for k in neighbour(i, j):
            if N > k[0] > -1 and N > k[1] > -1:
                R[dd(i, j)][dd(k[0], k[1])] = -1

sol = solve_lineqs(R, b)
print(2 * (sol[0] - sol[dd(1, 2)]))
print(4 / np.pi - 1 / 2)
end = time.time()
print(end-start)
