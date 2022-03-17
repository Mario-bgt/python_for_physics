def prime(n):
    out = list()
    for num in range(1, n + 1):
        pr = True
        for i in range(2, num):
            if num % i == 0:
                pr = False
        if pr:
            out.append(num)
    return out


def fib(n):
    prim = prime(4000)
    f = [19, 21]
    for n in range(2, n + 1):
        t = f[n - 1] + f[n - 2]
        if t in prim:
            f.append(t)
        else:
            for i in prim[1:]:
                if t % i == 0:
                    t = t//i
                    f.append(t)
                    break
    return f


print(fib(29))
