def Series(a, b, c, z):
    tk = 1
    eps = 0.0001
    summe = 1
    k = 1
    while True:
        up = (a + k - 1) * (b + k - 1)
        down = (c + k - 1) * k
        part = up / down
        tk = part * z * tk
        summe = summe + tk
        k = k + 1
        if abs(tk) < eps:
            return summe


z = float(input("gib nummier:"))  # -0.234647
Sol = Series(1, 1, 2, z)
print("Seri ischt:", Sol)
