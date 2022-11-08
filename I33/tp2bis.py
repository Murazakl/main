def ens_to_int(A):
    t = 0
    for i in range (len(A)):
        t = t | (1<<A[i])
    return t

def int_to_ens(t):
    L = []
    A = []
    i = 0
    while t != 0:
        L += [t & 1]
        t = t >> 1
        if (L[i] == 1):
            A += [i]
        i += 1
    return A

def ajout_dans(t,e):
    return (1<<e) | t

def retire_dans(t,e):
    return (1<<e) ^ t

def est_dans(t,e):
    return t | (1<<e) == t

def est_inclus_dans(t1,t2):
    return t1 & t2 == t1

def intersection(t1,t2):
    return t1 & t2

def union(t1,t2):
    return t1 | t2

def difference(t1,t2):
    return t1 ^ ((t1|t2) & (t1&t2))

def difference_sym(t1,t2):
    return t1 ^ t2

def euclide_e(a,n):
    u1 = 1
    v1 = 0
    u = 0
    v = 1
    while (n != 0):
        q = a // n
        r = a % n
        a , n = n , r
        w = u1 - q * u
        w1 = v1 - q * v
        u1 , v1 = u , v
        u , v = w , w1
    return [u1,v1,a]

def inverse(a,p):
    u=1
    v=0
    u1=0
    v1=1
    p_ = p
    while p != 0:
        r = a % p
        q = a // p
        a , p = p , r
        w = u - q * u1
        w1 = v - q * v1
        u , v = u1 , v1
        u1 , v1 = w , w1
    return u % p_

def euler_phi(n):
    cpt = 1
    i = 2
    while  i < n :
        a = n
        b = i
        while a != 0:
            b,a = a, b % a
        if b == 1:
            cpt += 1
        i += 1
    return cpt

def puissance(x,y,n):
    result = 1
    while y > 0:
        if y&1 > 0:
            result = (result * x) % n
        y >>= 1
        x = (x * x) % n    
    return result

t1 = 9470491
t2 = 33305
print(difference2(t1,t2))
