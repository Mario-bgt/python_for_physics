def newton(f, Df, xn):
    epsilon = 1e-320
    n = 0
    while True:
        if n > 10000:
            return xn
        if f(xn)/Df(xn) < epsilon:
            return xn
        xn = xn - f(xn)/Df(xn)
        n += 1