def newton(f, Df, xn):
    epsilon = 1e-300
    while True:
        if f(xn) / Df(xn) < epsilon:
            print(xn)
            break
        xn = xn - f(xn) / Df(xn)


def f(x):
    j = x ** 3 + x - 64
    return j


def Df(x):
    j = 3 * x ** 2 + 1
    return j


xn = 4

newton(f, Df, xn)
