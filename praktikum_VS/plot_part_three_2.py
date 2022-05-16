import numpy as np
import matplotlib

matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

fig = plt.figure()

pa = [175000, 170000, 165000, 160000,
      155000, 150000, 145000, 140000, 135000, 130000, 125000, 120000, 115000, 110000]
T = [393.15, 392.15, 391.15, 390.65,
     389.15, 388.15, 387.15, 387.15, 385.65, 384.15, 383.15, 382.15, 381.15, 379.15]

xerr= []
for j in T:
    h = j + 0.5
    t = j - 0.5
    xerr.append((1/h - 1/t)/50)


yerr = 0.02
x = []
for i in pa:
    x.append(1/i)
y = np.log(pa)

step_x = [
    x[0], x[-1]
]
step_y = [
    y[0]+0.02, y[-1]-0.02
]
low_y = [
    y[0]-0.02, y[-1]+0.02
]
steepest = (step_y[1]-step_y[0])/(step_x[1]-step_x[0])
flattest = (low_y[1]-low_y[0])/(step_x[1]-step_x[0])
print('Steppest is', -steepest*8.3144)
print('Flattest is', -flattest*8.3144)
c_step = step_y[0]-step_x[0]*steepest
c_flat = low_y[0]-step_x[0]*flattest
x_crit = np.linspace(min(x)*0.97,max(x)*1.02, 100)
print('m is ', (-steepest*8.3144 + flattest*8.3144)/2 )

plt.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, fmt='.k', elinewidth=0.5, markersize=0.5, capsize=1, color="black", label=r'$ln_{PD}(T)$')
plt.plot(x_crit, x_crit*steepest + c_step, linewidth='0.5', linestyle='dashed', color='red',
         label=r'$steepest\:line\:within\:error\:m=-1.49352\cdot 10^5 $')
plt.plot(x_crit, x_crit*flattest + c_flat, linewidth='0.5', linestyle='dashed', color='blue',
         label=r'$flattest\:line\:within\:error\:m=-1.25659\cdot 10^5 $')
slope_intercept = np.polyfit(x, y, 1)
print(slope_intercept)
print((-slope_intercept[0])*8.3144)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth='0.5', linestyle='dashed', color='black',
         label=r'$ln_{PD}(T) = -1.37914339 \cdot 10^{5} \:T  + 12.84 $')
plt.ylabel(r'$\ln(pa)$')
plt.xlabel(r'$1/T$')
plt.grid(color='k', linestyle='--', linewidth=0.2)
plt.legend(loc='best')
plt.savefig('graph_3_2.pdf')
plt.show()
