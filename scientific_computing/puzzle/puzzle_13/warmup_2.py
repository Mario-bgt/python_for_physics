import numpy as np


def solve_lineqs(A, b):
    wert, Vek = np.linalg.eigh(A)
    wert = 1 / wert
    Ainv = Vek @ np.diag(wert) @ Vek.T
    return Ainv @ b


'''
R = 1
R2 = 0.87
u = (i1+i2)*R2+i1*R+(i1+i3)*R = i1*R2+i2*R2+i1*R+i1*R+i3*R 
U = (i1+i2)*R2+i2*R+(i2+i5)*R = i1*R2+i2*R2+i2*R+i2*R+i5*R
U = (i3+i4)*R+R*i3+(i1+i3)*R = i3*R+i4*R+i3*R+i1*R+i3*R
U = (i3+i4)*R+i4*R+(i4+i6)*R = i3*R+i4*R+i4*R+i4*R+i6*R
U = (i5+i6)*R + i5*R + (i5+i2)*R = i5*R+i6*R+i5*R + i5*R+i2*R
U = (i5+i6)*R + i6*R + (i6+i4)*R = i5*R + i6*R + i6*R + i4*R + i6*R
==>
U = i1*(2*R+R2)+i2*R2+i3*R
U = i1*R2+i2*(R2+2*R)+i5*R
U = i1*R + i3*3*R + i4*R
U = i3*R+i4*3*R+i6*R
U = i2*R+i5*3*R+i6*R
U = i4*R + i5*R + i6*3*R
'''
R = 1
R2 = 0.87
A = [[2 * R + R2, R2, R, 0, 0, 0],
     [R2, R2 + 2 * R, 0, 0, R, 0],
     [R, 0, 3 * R, R, 0, 0],
     [0, 0, R, 3 * R, 0, R],
     [0, R, 0, 0, 3 * R, R],
     [0, 0, 0, R, R, 3 * R]]

b = [[1], [1], [1], [1], [1], [1], ]
I = solve_lineqs(A,b)
I_tot = np.sum(I)
print(1/I_tot)