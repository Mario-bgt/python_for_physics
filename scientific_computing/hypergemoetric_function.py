def Series(a, b, c, z):
    Tk = 1
    eps = 0.0001
    Sum = 1
    k = 1
    while True:
        up = (a + k - 1) * (b + k - 1)
        down = (c + k - 1) * k
        part = up / down
        Tk = part * z * Tk
        Sum = Sum + Tk
        k = k + 1
        if abs(Tk) < eps:
            return Sum


z = float(input("gib nummier:"))  # -0.234647
Sol = Series(1, 1, 2, z)
print("Seri ischt:", Sol)
