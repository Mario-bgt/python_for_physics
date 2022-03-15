from fractions import Fraction


def factorials(n):
    f = [1, 1]
    for i in range(2, n + 1):
        f.append(f[(i - 1)] * i)
    return f


def bernoulli(m):
    b = [Fraction(1, 1), Fraction(-1, 2)]
    f = factorials(4000)
    for i in range(2, m):
        k = 0
        summe = 0
        while True:
            up = int(f[i] * b[k])
            down = int(f[k] * f[(i - k + 1)])
            summe = summe + Fraction(up, down)
            k += 1
            if k == i:
                b.append(-1 * summe)
                break
    return b


baba = bernoulli(55)
print(baba[50])
