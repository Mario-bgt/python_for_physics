import csv
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

plt.rcdefaults()

index = ('CHE', 'POL', 'USA', 'UKR', 'AUT', 'FRA', 'IRL', 'HRV', 'DEU')
countries = (['Switzerland', 'Poland', 'USA', 'Ukraine', 'Austria', 'France', 'Ireland', 'Croatia', 'Germany'])
color = (['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'pink', 'purple', 'black'])
for t in range(1995, 2014):
    plt.gca().clear()
    y = []
    for i in index:
        y.append(rail_per_pop[i][t])
    print(y)
    plt.bar(countries, y, color=color)
    plt.xticks(countries)
    plt.ylabel('Amount of track per person')
    plt.title('Railwaytrack per person in the year ' + str(t))
    plt.pause(2)

plt.show()
