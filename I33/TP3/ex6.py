def multbyalpha(b, f):
    resultat = b << 1
    taille = len(bin(f)) - 3
    if ((resultat & (1 << taille)) != 0):
        resultat ^= f
    return resultat


def table_log(P):
    taille = len(bin(P)) - 3
    deca = 1 << taille
    L = [-1] * deca
    i, j = 1, 0
    while j < deca - 1:
        L[i], i = j, multbyalpha(i, P)
        j += 1
    return L

