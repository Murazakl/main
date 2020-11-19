def is_irreducible(P,p):
    irre = True
    b = 0
    while (b < p) and irre:
        val = P[0]
        for i in range(1, len(P)):
            val = (val * b + P[i]) % p
        irre = (val != 0)
        b += 1
    return irre

print(is_irreducible(6,3))    