def decompose(n):
    L, i = [], 2
    cpt = 0
    while n != 1:
        if n % i == 0:
            cpt += 1
            n //= i 
            L += [i,cpt]
        else: 
            i += 1
            cpt = 0
    return L

print(decompose(99999876400))

