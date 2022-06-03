from fractions import Fraction


def arctan(frac):
    t_old = res = x = frac
    k = 1
    eps = Fraction(1, 10**100)
    while True:
        t = (-x ** 2) * t_old
        res = res + Fraction(t, 2 * k + 1)
        t_old = t
        k += 1
        if abs(Fraction(t, 2 * k + 1)) < eps:
            return res


def pi(alpha, beta):
    return 4 * (arctan(alpha) + arctan(beta))


def frac_to_string(frac):
    pn = int(frac)
    pf = frac - pn
    pf1000 = int(10 ** 100 * pf)
    return str(pn) + '.' + str(pf1000)

