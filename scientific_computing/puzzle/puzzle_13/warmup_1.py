import numpy as np


def solve_lineqs(A, b):
    wert, Vek = np.linalg.eigh(A)
    wert = 1 / wert
    Ainv = Vek @ np.diag(wert) @ Vek.T
    return Ainv @ b


R = np.array([[2, -1, -1, 0],
              [-1, 3, -1, 1],
              [-1, -1, 3, -1],
              [0, -1, -1, 2]])
b = np.array([[1],
              [0],
              [0],
              [-1]])

res = solve_lineqs(R, b)
print(res)
print(res[0] - res[3])
print(R)
