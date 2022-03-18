import csv

filename = 'rail_lines.csv'
file = open(filename, encoding='utf-8')
table = csv.reader(file, delimiter=',', quotechar='"')
table = list(table)

rail = {}
for i, row in enumerate(table[4:20]):
    for j, col in enumerate(row):
        if col != '':
            if i not in rail:
                rail[i] = {}
            rail[i][j] = col

for r in rail:
    print(r, rail[r])
