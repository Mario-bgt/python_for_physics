from fractions import Fraction


def arctan(a, b, e):
    """This function takes two int (a and b) as an input,
    and then calculates the arctan of the fraction a/b. e represents
    the amount  of repetition for the taylor sum to calculate arctan, the greater e is
    the more accurate is the result."""
    t_old = res = x = Fraction(a, b)
    k = 1
    eps = e
    while True:
        t = (-x ** 2) * t_old
        res = res + Fraction(t, 2 * k + 1)
        t_old = t
        k += 1
        if k == eps:
            return res


def pi(e):
    """This function returns pi as a fraction, with e being as
    described in def arctan"""
    return 4 * (arctan(1, 2, e) + arctan(1, 3, e))


def frac_to_string(frac):
    """This function turns a fraction into the string of the decimal number to 1000 places"""
    pn = int(frac)
    pf = frac - pn
    pf1000 = int(10 ** 10000 * pf)
    return str(pn) + '.' + str(pf1000)


pi = frac_to_string(pi(5000))
print(pi[941:955])
print(pi)
