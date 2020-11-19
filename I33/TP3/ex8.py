def is_primitif(P):
    m = len(P) - 1
    div = decompose((1 << m) - 1)
    continu = True
    j = 0
    while j < len(div) and continu:
        z = 1
        y = ((1 << m) - 1) // div[j]
        x = 2
        while y != 0:
            if ( y & 1):
                z = multiplie(z,x,P)
            x = multiplie(x,x,P)
            y = y >> 1
        continu = ((z != 1) and (z != 0))
        j += 1
    return ((j == len(div)) and (continu == True))