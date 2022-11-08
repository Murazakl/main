def combinaison_lineaire(c,V):
    L = []
    for i in range(len(V[0])):
        s = 0
        for j in range(len(c)):
            s += c[j] * V[j][i]
        L += [s]
    return L
        
def combinaison_lineaire2(c,V):
    s = 0
    i = len(V) - 1
    while i >= 0:
        if c & 1:
            s = s ^ V[i]
        i -= 1
        c = c >> 1
    return s

def combinaison_lineaire(c,V,p):
    L = []
    for i in range(len(V[0])):
        s = 0
        for j in range(len(c)):
            s += c[j] * V[j][i]
        L += [s%p]
    return L

def liste_vecteurs(n):
    L = []
    for i in range(1 << n):
        L2 = []
        j = i
        v = n
        while v != 0:
            L2 = [j&1] + L2
            j = j >> 1
            v -= 1
        L += [L2]
    return L

def liste_vecteurs2(p,n):
    L = []
    for i in range((p**n)):
        L2 = []
        j = i
        v = n
        while v != 0:
            L2 = [j%p] + L2
            j //= p
            v -= 1
        L += [L2]
    return L

def build_Vect(relation):
    L = []
    i = 1
    while i < len(relation):
        L2 = [0] * len(relation)
        L2[0] = -relation[i]/relation[0]
        L2[i] = 1
        L += [L2]
        i += 1
    return L

def vect(L):
    Lres, i = [], len(L[0])
    for j in range(1 << len(L)):
        l, k, L2 = j, 0, [0] * i
        while l != 0:
            if l & 1:
                for m in range(i):
                    L2[m] = L2[m] ^ L[k][m]
            k += 1
            l = l >> 1
        Lres += [L2]
    return Lres


print(vect([[1,0,0,1], [0,1,1,1], [1,1,0,1],[1,0,1,0]]))
    
