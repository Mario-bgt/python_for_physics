a = 2
b = 3
if a == 3:
    a = a + 1
elif b == 3:
    b = b*2
    if b == 4:
        b = b + 5
    elif a == 3:
        b = b + 6
else:
    b = b - 1
print(b)