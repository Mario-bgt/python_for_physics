def newton(f, Df, xn):
    xold = [xn]
    n = 0
    while True:
        xn = xn - f(xn)/Df(xn)
        if xn in xold:
            print('it took',n,'iterations to compile')
            return xn
        xold.append(xn)
        n += 1


def f(x):
    j = x ** 3 + x - 64
    return j


def Df(x):
    j = 3 * x ** 2 + 1
    return j


xn = 4

print(newton(f, Df, xn))
