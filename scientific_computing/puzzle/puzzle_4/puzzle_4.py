import csv

filename = 'exoplanets.csv'
file = open(filename, encoding='utf-8')
table = csv.reader(file, delimiter=',')
table = list(table)

exoplanet = {}
for i, row in enumerate(table[1:]):
    for j, col in enumerate(row[2:3]):
        if col != '':
            if row[0] not in exoplanet:
                exoplanet[row[0]] = {}
            exoplanet[row[0]]['mass'] = float(col)
    for j, col in enumerate(row[86:87]):
        if col != '':
            if row[0] not in exoplanet:
                exoplanet[row[0]] = {}
            exoplanet[row[0]]['star_radius'] = float(col)
    for j, col in enumerate(row[15:16]):
        if col != '':
            if row[0] not in exoplanet:
                exoplanet[row[0]] = {}
            exoplanet[row[0]]['semi_major_axis'] = float(col)
    for j, col in enumerate(row[93:94]):
        if col != '':
            if row[0] not in exoplanet:
                exoplanet[row[0]] = {}
            exoplanet[row[0]]['star_teff'] = float(col)

for i in exoplanet:
    print(i, exoplanet[i])

#star_radius index 86
#semi_major_axis index 15
#star_teff mass 93