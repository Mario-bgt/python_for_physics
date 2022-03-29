import csv
import time

start = time.time()

filename = 'exoplanets.csv'
file = open(filename, encoding='utf-8')
table = csv.reader(file, delimiter=',')
table = list(table)
header = table[0:1][0]
key = ('mass', 'star_radius', 'semi_major_axis', 'star_teff')

ep = {}
for row in table[1:]:
    for i, cell in enumerate(row):
        if header[i] in key:
            if cell != '':
                if row[0] not in ep:
                    ep[row[0]] = {}
                ep[row[0]][header[i]] = cell

k = 0
exoplanets = list()
for i in ep:
    if 'mass' in ep[i] and 'star_radius' in ep[i] and 'semi_major_axis' in ep[i] and 'star_teff' in ep[i]:
        m = float(ep[i]['mass']) * 340
        s = (float(ep[i]['star_radius']) ** 2) * ((float(ep[i]['star_teff']) / 5800) ** 4) * (
                    (float(ep[i]['semi_major_axis'])) ** (-2))
        if 1.5 > m > 0.6 and 5 > s > 0.2:
            k += 1
            print(i, m, s, ep[i])
            exoplanets.append(i)
print('We found', k, 'earth like exoplanets with a mass between max 1.5 times earth mass and min 0.6 times earth mass.')
print('The daylight strength relative to the Earth is at max 5 times and at min 0.2 times the one of earth.')
print('The following exoplanets were found:')
for planets in exoplanets:
    print(planets)

end = time.time()
print('It took', (end - start), 'seconds to execute.')
