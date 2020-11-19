import random
import copy

def genmatrix(n,p,t):
    L = [[0] * p for i in range (n)]
    i = 0
    while i < n:
        j = 0
        while j < p:
            L[i][j] = random.randrange(0, t)
            j += 1
        i += 1
    return L


def gendiag(n,t):
    L = [0] * n 
    for i in range (n):
        L[i] = [0] * n
        L[i][i] = random.randrange(0, t)
    return L

def gentrianginf(n,t):
    L = [0] * n
    for i in range (n):
        L[i] = [0] * n
        for j in range (i+1):
            L[i][j] = random.randrange(0, t)
    return L

def gensym(n,t):
    L = gentrianginf(n,t)
    for i in range(n):
        for j in range(i + 1, n):
            L[i][j] = L[j][i]
    return L

def genasym(n,t):
    L = gentrianginf(n,t)
    for i in range(n):
        for j in range(i,n):
            L[i][j] = -L[j][i]
    return L

def transpose(M):
    n = len(M)
    c = len(M[0])
    L = [[M[j][i] for j in range (n)] for i in range (c)]
    return L

def gencirculante(L):
    L2 = [L[i::] + L[:i:] for i in range (1,len(L)+1) [::-1]]
    return L2

def gencirculante2(k,t):
    L = [k]
    for i in range(1, t):
        x = L[i-1] & 1
        y = x << (t-1)
        L += [(L[i-1] >> 1) ^ y]
    return L

def liste_perm(n):
    L = []
    for i in range(n):
        L += [i]
    j = 1
    while j < n:
        perm = random.randrange(0, n-j)
        tmp = L[perm]
        L[perm] = L[n-j]
        L[n-j] = tmp
        j += 1
    return L

def genmatrixperm(n):
    L = [0] * n
    liste = liste_perm(n)
    for i in range(n):
        L[i] = [0] * n
        L[i][liste[i]] = 1
    return L
    
print(genmatrixperm(3))
