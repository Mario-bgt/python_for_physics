import csv
import matplotlib.pyplot as plt
import time

non_countries = ['ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA',
                 'ECS', 'EMU', 'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA',
                 'IDB', 'IDX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE',
                 'MEA', 'MIC', 'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST',
                 'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA',
                 'TSS', 'UMC', 'WLD']


def dic(filename):
    file = open(filename, encoding='utf-8')
    table = csv.reader(file, delimiter=',', quotechar='"')
    table = list(table)
    head = table[4:5][0][4:]
    newdic = {}
    for i, row in enumerate(table[5:]):
        if row[1] not in non_countries:
            for j, col in enumerate(row[4:]):
                if col != '':
                    if row[1] not in newdic:
                        newdic[row[1]] = {}
                    newdic[row[1]][int(head[j])] = float(col)
    return newdic


rail_per_pop = {}
population = dic('population.csv')
rail = dic('rail_lines.csv')
for i in dic('population.csv'):
    for k in dic('rail_lines.csv'):
        if k == i:
            for j in range(1995, 2020):
                if j in population[i] and j in rail[k]:
                    if i not in rail_per_pop:
                        rail_per_pop[i] = {}
                    rail_per_pop[i][j] = (rail[k][j] * 1000) / population[i][j]


plt.rcdefaults()

index = ('CHE', 'POL', 'UKR', 'AUT', 'FRA', 'IRL', 'HRV', 'FIN', 'SWE', 'TKM')
countries = (['Switzerland', 'Poland', 'Ukraine', 'Austria', 'France', 'Ireland', 'Croatia', 'Finland', 'Sweden', 'Turkmenistan'])
color = (['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'pink', 'purple', 'black','red'])
for t in range(1995, 2020):
    start = time.time()
    plt.gca().clear()
    y = []
    for i in index:
        if t not in rail_per_pop[i]:
            y.append(0)
        else:
            y.append(rail_per_pop[i][t])
    plt.bar(countries, y, color=color)
    plt.xticks(countries)
    plt.ylabel('Amount of track per person')
    plt.title('Railwaytrack per person in the year ' + str(t))
    end = time.time()
    print(end-start)
    plt.pause(1)

plt.show()
