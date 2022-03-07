from fractions import Fraction


def arctan(a, b):
    """This function takes two int (a and b) as an input,
    and then calculates the arctan of the fraction a/b"""
    t_old = res = x = Fraction(a, b)
    k = 1
    eps = 3000
    while True:
        t = (-x ** 2) * t_old
        res = res + Fraction(t, 2 * k + 1)
        t_old = t
        k += 1
        if k == eps:
            return res


def pi():
    """This function returns pi as a fraction"""
    return 4 * (arctan(1, 2) + arctan(1, 3))


def frac_to_string(frac):
    """This function turns a fraction into the string of the decimal number to 1000 places"""
    pn = int(frac)
    pf = frac - pn
    pf1000 = int(10 ** 10000 * pf)
    return str(pn) + '.' + str(pf1000)


pi = frac_to_string(pi())
print(pi[941:955])
# print(pi[2:8])
print(pi)
