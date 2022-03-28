import csv
import numpy as np
import matplotlib.pyplot as plt

non_countries = ['ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA',
                 'ECS', 'EMU', 'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA',
                 'IDB', 'IDX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE',
                 'MEA', 'MIC', 'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST',
                 'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA',
                 'TSS', 'UMC', 'WLD']

filename1 = 'rail_lines.csv'
file1 = open(filename1, encoding='utf-8')
table1 = csv.reader(file1, delimiter=',', quotechar='"')
table1 = list(table1)
header = table1[4:5][0][4:]

rail = {}
for i, row in enumerate(table1[5:]):
    if row[1] not in non_countries:
        for j, col in enumerate(row[4:]):
            if col != '':
                if row[1] not in rail:
                    rail[row[1]] = {}
                rail[row[1]][int(header[j])] = float(col)

filename2 = 'population.csv'
file2 = open(filename2, encoding='utf-8')
table2 = csv.reader(file2, delimiter=',', quotechar='"')
table2 = list(table2)
header = table2[4:5][0][4:]

population = {}
for i, row in enumerate(table2[5:]):
    if row[1] not in non_countries:
        for j, col in enumerate(row[4:]):
            if col != '':
                if row[1] not in population:
                    population[row[1]] = {}
                population[row[1]][int(header[j])] = float(col)

rail_per_pop = {}
for i in population:
    for k in rail:
        if k == i:
            for j in range(1995, 2020):
                if j in population[i] and j in rail[k]:
                    if i not in rail_per_pop:
                        rail_per_pop[i] = {}
                    rail_per_pop[i][j] = (rail[k][j] * 1000) / population[i][j]

for i in rail_per_pop:
    print(i, rail_per_pop[i])


def timevar(indic, c, year):
    x = []
    y = []
    for t in range(1995, year):
        if t in indic[c]:
            x.append(t)
            y.append(indic[c][t])
    return x, y


for year in range(1996, 2015):
    plt.gca().clear()
    x, y = timevar(rail_per_pop, 'CHE', year)
    plt.plot(x, y, label='Switzerland')
    x, y = timevar(rail_per_pop, 'POL', year)
    plt.plot(x, y, label='Poland')
    x, y = timevar(rail_per_pop, 'USA', year)
    plt.plot(x, y, label='USA')
    x, y = timevar(rail_per_pop, 'UKR', year)
    plt.plot(x, y, label='Ukraine')
    x, y = timevar(rail_per_pop, 'AUT', year)
    plt.plot(x, y, label='Austria')
    x, y = timevar(rail_per_pop, 'FRA', year)
    plt.plot(x, y, label='France')
    x, y = timevar(rail_per_pop, 'IRL', year)
    plt.plot(x, y, label='Ireland')
    x, y = timevar(rail_per_pop, 'HRV', year)
    plt.plot(x, y, label='Croatia')
    plt.xticks(range(1995,year,1))
    plt.xlabel('From 1995 till ' + str(year))
    plt.ylabel('Railwaytrack per person in meters')
    plt.title('Different amount of railway tracks per person of countries')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
               fancybox=True, shadow=True, ncol=5)
    plt.pause(2)
plt.show()
