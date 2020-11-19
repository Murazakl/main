def recherche(L,S,p):
    T = []
    k = 0
    while k < len(L) - p:
        som = L[k]
        i = k + 1
        while i <= p + k:
            som += L[i]
            i += 1
        if som >= S:
            T += [k]
        k += 1
    return T

