import numpy as np

m_W = 0.48
c_W= 4187
W = 127.7
T_1 = 321.35
T_G = 285.65
m_E = 0.3978
T_E = 273.15
l_S = 3.338*10**5

res = ((m_W*c_W+W)*(T_1-T_G)-m_E*c_W*(T_G-T_E))/m_E
print(res)

res2 = (l_S*m_E+m_E*c_W*(T_G-T_E))/(T_1-T_G)-m_W*c_W
print(res2)

res = ((m_W*c_W+res2)*(T_1-T_G)-m_E*c_W*(T_G-T_E))/m_E
print(res,l_S)

m_B = 0.382
T_G = 310.2
T_B = 284.15
T_A = 322.15
m_A = 0.300

res = m_B*c_W*((T_G-T_B)/(T_A-T_G))-m_A*c_W
print(res)
m_W = 0.48
c_W= 4187
W = 127.7
T_1 = 321.35
T_G = 285.65
m_E = 0.3978
T_E = 273.15
l_S = 3.338*10**5
res2 = ((m_W*c_W+2230.53)*(T_1-T_G)-m_E*c_W*(T_G-T_E))/m_E
print(res2,l_S)