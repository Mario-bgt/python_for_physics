import csv
import numpy as np

year = str(input('From what year do you want to know the highest amount of track per person?'))
filename1 = 'rail_lines.csv'
file1 = open(filename1, encoding='utf-8')
table1 = csv.reader(file1, delimiter=',', quotechar='"')
table1 = list(table1)
header = table1[4:5][0][4:]

rail = {}
for i, row in enumerate(table1[5:]):
    for j, col in enumerate(row[4:]):
        if col != '':
            if row[1] not in rail:
                rail[row[1]] = {}
            rail[row[1]][header[j]] = float(col)
        else:
            if row[1] not in rail:
                rail[row[1]] = {}
            rail[row[1]][header[j]] = 0

filename2 = 'population.csv'
file2 = open(filename2, encoding='utf-8')
table2 = csv.reader(file2, delimiter=',', quotechar='"')
table2 = list(table2)
header = table2[4:5][0][4:]

population = {}
for i, row in enumerate(table2[5:]):
    for j, col in enumerate(row[4:]):
        if col != '':
            if row[1] not in population:
                population[row[1]] = {}
            population[row[1]][header[j]] = float(col)
        else:
            if row[1] not in population:
                population[row[1]] = {}
            population[row[1]][header[j]] = 0

if year == 'all':
    yeet = np.linspace(1960, 2015, 56)
    for y in yeet:
        j = str(y)[:-2]
        maximum = float(0)
        maximum_i = ''
        for i in rail:
            if rail[i][j] != 0 and population[i][j] != 0:
                track_per_pop = (rail[i][j]) * 1000 / (population[i][j])
                if track_per_pop > maximum:
                    maximum = track_per_pop
                    maximum_i = i
        if maximum_i != '':
            print('In the year', j, 'the country with the most track per person is:\n', str(maximum_i), str(maximum))
else:
    maximum = float(0)
    maximum_i = ''
    for i in rail:
        if rail[i][year] != 0 and population[i][year] != 0:
            track_per_pop = (rail[i][year]) * 1000 / (population[i][year])
            if track_per_pop > maximum:
                maximum = track_per_pop
                maximum_i = i
    print('In the year', year, 'the country with the most track per person is:\n', str(maximum_i), str(maximum))
