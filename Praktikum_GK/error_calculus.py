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
values2 = [35.5,
           32.1,
           25.2,
           17.8,
           12,
           10,
           11.5,
           16.5,
           22,
           26.7,
           29,
           28.3,
           25.1,
           21,
           17.1,
           15.2,
           14.2,
           16.1,
           19.5,
           22.8,
           25.3,
           25.8,
           24.5,
           22.1,
           19.5,
           17.5,
           16.6,
           17.2,
           18.9,
           21.1,
           22.9,
           23.6,
           23.3,
           22.3,
           20.6,
           19.1,
           18.1,
           18,
           18.8,
           20.1,
           21.5,
           22.3,
           22.6]
y = int(len(values))
x = 0

for i in values:
    x += i
x = (x / y)
# print('Der Wert für P_end ist gleich ' + str(2*x))

error = 0
for i in values:
    error += (i - x) ** 2

error = np.sqrt((1 / (y * (y - 1))) * error)
# print('Der Fehler auf P_end ist gleich '+str(2*error))

T = 630
tau = -2846.939075
r = 0.047
d = 0.050
S = 0.179
M = 1.5
L = 5.38
m_t = 15.159
m_tau = 21.442
m_S = 0.00799
temp = ((4 * np.pi ** 2) / T ** 2) + (1 / tau ** 2)
G = (temp * (r ** 2) * d * S) / (4 * M * L)
print('G is equal to ' + str(G))

mt = (-(((2*np.pi**2)*d*S)/(4*L*M*(T**3)))*m_t)**2
print('Der Fehler auf T ist '+str(mt))
mtau = (-((d*(r**2)*S)/(4*L*M*(tau**2)))*m_tau)**2
print('Der Fehler auf Tau ist gleich: '+str(mtau))
ms = (((4*(np.pi**4)*d*(r**2)*tau+d*(r**2)*(T**2))/(4*L*M*(T**2)*tau))*m_S)**2
print('Der Fehler auf S ist gleich: '+str(ms))
print(mt+mtau+ms)
print('Der gesammte Fehler auf G ist gleich: '+str(np.sqrt(ms+mtau+mt)))



G = 6.6742 * (10 ** (-11))

temp = (4 * G * M * L) / ((r ** 2) * d * S) - (4 * np.pi ** 2) / (T ** 2)
tau = 1 / (np.sqrt(temp))
print('Tau is equal to ' + str(tau))
