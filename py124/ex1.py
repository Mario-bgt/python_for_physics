b = 2
def add(a):
    c = b + 2
    b = c + a
    return b
b = add(3)
print(b)