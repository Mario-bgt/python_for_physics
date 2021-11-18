import numpy as np

values = [318,
312.6,
314.4,
323.4,
302.4,
277.8,
343.8,
344.4,
286.2

          ]
x = 313.6666667


error = 0
for i in values:
    error += (i-x)**2

error = np.sqrt(error/42)
print(error)


T = 630
tau = -0.04876
r = 0.047
d = 0.050
S = 0.179
M = 1.5
L = 5.38
G = 6.6742*(10**(-11))

#temp = ((4*np.pi**2)/T**2)+(1/(tau**2))
#G = (temp*(r**2)*d*S)/(4*M*L)

temp = (4*G*M*L)/((r**2)*d*S)-(4*np.pi**2)/(T**2)
print(temp)
tau = 1/(np.sqrt(temp))
print(G)
print(tau)