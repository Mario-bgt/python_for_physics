def has9(n):
    s = str(n)
    for c in s:
        if c == '9':
            return True
    return False


max = 2 ** 30000
pov = 1
last = 1

while pov < max:
    if not has9(pov):
        last = pov
    pov *= 2

print(last)
