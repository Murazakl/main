def decompose(n):
    L, i = [], 3
    if (n % 2 == 0):
        cpt = 0
        while (n % 2) == 0:
            n = n // 2
            cpt += 1
        L += [2,cpt]
    while n != 1:
        cpt = 0
        if (n % i) == 0:
            while (n % i) == 0:
                n = n // i
                cpt += 1
            L += [i,cpt]
        i = i + 2
    return L

def decompose2(n):
    L = []
    while n != 0:
        L = [n & 1] + L
        n = n >> 1
    return L
