import numpy as np


e_11 = 1 / (2 * np.sqrt(21))
e_12 = 3 / (2 * np.sqrt(21))
e_13 = 5 / (2 * np.sqrt(21))
e_14 = 7 / (2 * np.sqrt(21))

p = [[e_11], [e_12], [e_13], [e_14]]
q = [[e_11, e_12, e_13, e_14]]
matrix1 = np.dot(p, q)
print("Result of matrix1 multiplication:")
print(matrix1)

e_21 = 136 / (16 * np.sqrt(105))
e_22 = 72 / (16 * np.sqrt(105))
e_23 = 8 // (16 * np.sqrt(105))
e_24 = -56 / (16 * np.sqrt(105))

r = [[e_21], [e_22], [e_23], [e_24]]
s = [[e_21, e_22, e_23, e_24]]
matrix2 = np.dot(r, s)
print("Result of matrix2 multiplication:")
print(matrix2)

P_w = matrix1 + matrix2
print("P_w is equal to")
print(P_w)

I_d = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

P_wo = I_d - P_w
print('P_w ortho is equal to')
print(P_wo)