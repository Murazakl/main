def recherche2(L,S,p):
    T = []
    k = 0
    som = L[0]
    i = 1
    while i <= p:
        som += L[i]
        i += 1
    if som >= S:
        T += [0]
    k = 1
    while k < len(L) - p:
        som += L[p+k] - L[k-1]
        if som >= S:
            T += [k]
        k += 1
    return T