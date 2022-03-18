import csv

filename1 = 'rail_lines.csv'
file1 = open(filename1, encoding='utf-8')
table1 = csv.reader(file1, delimiter=',', quotechar='"')
table1 = list(table1)

rail = {}
for i, row in enumerate(table1[5:]):
    for j, col in enumerate(row[50:51]):
        if col != '':
            if row[1] not in rail:
                rail[row[1]] = {}
            rail[row[1]][2006] = float(col)

filename2 = 'population.csv'
file2 = open(filename2, encoding='utf-8')
table2 = csv.reader(file2, delimiter=',', quotechar='"')
table2 = list(table2)

population = {}
for i, row in enumerate(table2[5:]):
    for j, col in enumerate(row[4:]):
        if col != '':
            if row[1] not in population:
                population[row[1]] = {}
            population[row[1]][j + 1960] = float(col)

maximum = float(0)
maximum_i = ''
for i in rail:
    if rail[i][2006] != '' and population[i][2006] != '':
        track_per_pop = (rail[i][2006])*1000 / (population[i][2006])
        if track_per_pop > maximum:
            maximum = track_per_pop
            maximum_i = i

print(str(maximum_i), str(maximum))
