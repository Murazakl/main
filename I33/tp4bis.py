def eval_poly(P,b):
    i = 0
    j = len(P) - 1
    s = P[j]
    while i < len(P) and j > 0:
        s = (s * b) + P[j-1]
        i += 1
        j -= 1
    return s

def eval_poly2(P,b,p):
    i = 0
    j = len(P) - 1
    s = P[j]
    while i < len(P) and j > 0:
        s = ((s * b) + P[j-1]) % p
        i += 1
        j -= 1
    return s

def eval_poly_F2(P,b):
    i = 0
    j = len(P) - 1
    s = P[j]
    while i < len(P) and j > 0:
        s = (s & b) ^ P[j-1]
        i += 1
        j -= 1
    return s
    
def eval_poly_F22(P,b):
    i = 0
    L = []
    while P != 0 :
        L += [P%2]
        P = P // 2
    j = len(L) - 1
    s = L[j]
    while i < len(L) and j > 0:
        s = (s & b) ^ L[j-1]
        i += 1
        j -= 1
    return s

def is_irreductible(P,p):
    irr = True
    b = 0
    while (b < p) and irr: 
        val = P[0]
        for i in range(1,len(P)):
            val = (val * b + P[i]) % p 
        irr = (val != 0)
        b += 1
    return irr

def decompose(n):
    L=[]
    while n!=0:
        L += [n%2]
        n = n // 2
    return L

def is_primitif(P):
    n = len(P) - 1
    div = decompose((1 << n) - 1)
    oncontinue = True
    j = 0
    while j < len(div) and oncontinue:
        z = 1
        y = ((1 << n) - 1) // div[j]
        x = 2
        while y != 0:
            if (y & 1):
                z = multiplie(z,x,P)
            x = multiplie(x,x,P)
            y = y >> 1
        oncontinue = ((z != 1) and (z != 0))
        j += 1
    return ((j == len(div)) and (oncontinue == True))
    
def hammingweight(n):
    cpt = 0
    while (n != 0):
        cpt += n & 1
        n = n >> 1
    return cpt

def hammingweight2(n):
    cpt = 0
    while (n != 0):
        cpt += 1
        n = n & n - 1
    return cpt

print
