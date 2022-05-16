import numpy as np

N = 3
R = np.zeros((N ** 2, N ** 2))
np.fill_diagonal(R, 4)
b = np.zeros((N ** 2, 1))
b.fill(1)


def solve_lineqs(A, b):
    wert, Vek = np.linalg.eigh(A)
    wert = 1 / wert
    Ainv = Vek @ np.diag(wert) @ Vek.T
    return Ainv @ b


def dd(x, y):
    return y * N + x


def neighbour(x, y):
    return (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)


l = []
for i in range(N):
    R[i * N][i * N + N - 1] = -1
    R[i * N + N - 1][i * N] = -1
    R[i][N ** 2 - N + i] = -1
    R[N ** 2 - N + i][i] = -1
    for j in range(N):
        for k in neighbour(i, j):
            if N > k[0] > -1 and N > k[1] > -1:
                R[dd(i, j)][dd(k[0], k[1])] = -1


I_tot = np.sum(solve_lineqs(R,b))
print(1/I_tot)
