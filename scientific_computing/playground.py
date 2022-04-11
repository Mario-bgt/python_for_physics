foo = [0, 0, 0, 0, 0]

for k in range(5):
    foo[k] = k * k
for x in enumerate(foo):
    print(x)
