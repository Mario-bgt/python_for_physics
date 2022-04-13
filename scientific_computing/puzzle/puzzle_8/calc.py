def newton(f, Df, xn):
    xold = [xn]
    while True:
        xn = xn - f(xn)/Df(xn)
        if xn in xold:
            return xn
        xold.append(xn)