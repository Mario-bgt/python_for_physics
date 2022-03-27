with open('genetic_code.txt') as f:
    lines = f.readlines()

dna = {}
for c in lines:
    if c[4:-2] not in dna:
        dna[c[4:-2]] = list()
    dna[c[4:-2]].append(c[:3])

for i in dna:
    dna[i].sort()
    print(i, type(i), dna[i], type(dna[i]))

print(dna['Asparagin'][1])
