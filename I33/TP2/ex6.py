def valeur(L,b):
    p, somme = 1, 0
    i = 0
    while i < len(L):
        somme += L[::-1][i] * p
        p *= b
        i += 1
    return somme

print(valeur([3,2,1],5))