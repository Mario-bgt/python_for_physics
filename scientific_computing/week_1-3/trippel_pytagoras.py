for d in range (1,1001):
    dtemp = d**3
    for a in range (1,d):
        for b in range (1,a+1):
            for c in range (1,b+1):
                if a**3 + b**3 +c**3 == dtemp:
                    print(a,b,c,d)