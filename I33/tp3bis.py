from random import *

def pgcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def generateurs(n):
    L = [1]
    i = 2
    while (i < n):
        if pgcd(i, n) == 1:
            L += [i]
        i += 1
    return L

def sous_groupe_gen_add(a,n):
    L = [a]
    b = a
    while ((a % n) != 0):
        a =(a + b) % n
        L += [a]
    return L

def decompose(n):
    L, i = [], 3
    if n % 2 == 0:
        while n % 2 == 0:
            n /= 2
        L += [2]
    while n != 1:
        if n % i == 0:
            while n % i == 0:
                n /= i
            L += [i] 
        i += 2
    return L

def generateurs2(p):
    n = p
    L = decompose(n-1)
    L_gen = []
    for g in range(2,n-1):
        j = 0 
        oncontinue = True
        while j < len(L) and oncontinue:
            oncontinue = (pow(g,(n-1)//L[j],n) != 1)
            j = j + 1
        if oncontinue:
            L_gen += [g]
    return L_gen

def generateurs3(p):
    g = randrange(2, p - 1)
    while (pow(g, (p - 1) // 2, p) == 1):
        g = randrange(2,p - 1)
    return g

def sous_groupe_gen_mult(a,n):
    L = [a]
    b = a
    while ((a % n) != 1):
        a =(a * b) % n
        L += [a]
    return L

def ord(a,n):
    nsav = n
    while a != 0:
        n, a = a, n % a
    return nsav / n

def is_of_order(a,t,n):
    return n // pgcd(a,n) == t

def is_sym_add(x,y,n):
    return (x + y) % n == 0

def is_sym_mul(x,y,n):
    return (x * y) % n == 1

def is_sym_add(x,y):
    return x[0] * y[1] + x[1] * y[0] == 0

def is_sym_mul(x,y):
    return x[0] * y[0] == x[1] * y[1]

def ord(a,p):
    if (a==1):
        return 1
    i = 2
    ok = False
    omin = p
    while (i*i <= (p-1)) and (not(ok)):
        if ((p-1) % i == 0):
            o = i
            ok = (pow(a,o,p) == 1)
            if not(ok):
                otmp = (p-1)//i
                if (pow(a,otmp,p) == 1) and (otmp < omin):
                    omin = otmp
        i=i+1
    if not(ok) and omin != p :
        return omin
    elif not(ok):
        return p - 1
    else:
        return o

def is_of_order_mult(a,t,n):
    oncontinue = (pow(a,t,n) == 1) and (a != 1)
    j = 2
    while j*j <= t and oncontinue:
        if (t % j)==0:
            oncontinue = ((pow(a,j,n) != 1) and (pow(a,t//j,n) != 1))
        j += 1
    return oncontinue or ((a == 1) and (t == 1))

print(ord(7,24))
