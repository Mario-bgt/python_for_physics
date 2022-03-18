from fractions import Fraction


def factorials(n):
    f = [1, 1]
    for i in range(2, n):
        f.append(f[(i - 1)] * i)
    return f


def bernoulli(m):
    b = [Fraction(1, 1), Fraction(-1, 2)]
    f = factorials(m+1)
    for i in range(2, m):
        summe = 0
        for k in range(0, i):
            up = int(f[i] * b[k])
            down = int(f[k] * f[(i - k + 1)])
            summe = summe + Fraction(up, down)
        b.append(-summe)
    return b


baba = bernoulli(55)
print(baba[50])
