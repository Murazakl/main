def multbyalpha(b,f):
    result = b << 1
    taille = len(bin(f)) - 3
    if ((result & (1 << taille)) != 0):
        result = result ^ f
    return result

def table_alpha(P):
    m = len(bin(P)) - 3
    cardinal = (1 << m)
    L = [0]*(cardinal - 1)
    L[0] = -1
    z = 1
    i = 0
    while i < cardinal - 1: 
        L[i] = z
        z = multbyalpha(z,P)
        i += 1
    return L

print(table_alpha(13))