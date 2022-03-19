import csv

filename = 'exoplanets.csv'
file = open(filename, encoding='utf-8')
table = csv.reader(file, delimiter=',')
table = list(table)

ep = {}
for i, row in enumerate(table[1:]):
    for j, col in enumerate(row[2:3]):
        if col != '':
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['mass'] = float(col)
        else:
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['mass'] = 0
    for j, col in enumerate(row[85:86]):
        if col != '':
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['star_radius'] = float(col)
        else:
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['star_radius'] = 0
    for j, col in enumerate(row[14:15]):
        if col != '':
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['semi_major_axis'] = float(col)
        else:
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['semi_major_axis'] = 0
    for j, col in enumerate(row[92:93]):
        if col != '':
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['star_teff'] = float(col)
        else:
            if row[0] not in ep:
                ep[row[0]] = {}
            ep[row[0]]['star_teff'] = 0
k = 0
exoplanets = list()
for i in ep:
    if ep[i]['mass'] != 0 and ep[i]['star_radius'] != 0 and ep[i]['semi_major_axis'] != 0 and ep[i]['star_teff'] != 0:
        m = ep[i]['mass'] * 340
        s = (ep[i]['star_radius'] ** 2) * ((ep[i]['star_teff'] / 58000) ** 4) * ((ep[i]['semi_major_axis']) ** (-2))
        if 4 > m > 0.5 and 2 > s > 0.1:
            k += 1
            exoplanets.append(i)
print('We found', k, 'earth like exoplanets with a mass between max 4 times earth mass and min 0.5 times earth mass.')
print('The daylight strength relative to the Earth is at max 2 times and at min 0.1 times the one of earth.')
print('The following exoplanets were found:')
for planets in exoplanets:
    print(planets)
