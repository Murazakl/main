def multbyalpha(b, f):
    resultat = b << 1
    taille = len(bin(f)) - 3
    if ((resultat & (1 << taille)) != 0):
        resultat = resultat ^ f
    return resultat

def multiplication(b,c,f):
    prod, v = 0, c
    while (b != 0):
        if (b & 1) != 0:
            prod ^= v
        v = multbyalpha(v, f)
        b >>= 1
    return prod
