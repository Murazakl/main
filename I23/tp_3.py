def factorielle(n):
    s = 1
    for i in range(1,n+1):
        s*= i
    return s

def TrianglePascal(n):
    l = [[0]*(n+1) for p in range(n+1)]
    for n in range(n+1):
        if n == 0:
            l[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    l[n][0] = 1
                else:
                    l[n][k] = l[n-1][k-1] + l[n-1][k]
    return l


def binomial(n,p):
    bin = factorielle(n) / (factorielle(p) * (factorielle(n-p)))
    return bin

def phoque(n):
    if n == 1: return ["."]
    elif n == 2: return ["-",".."]

    n1 = []
    for i in phoque(n-1):
        n1 += [i + "."]
    n2 = []
    for j in phoque(n-2):
        n2 += [j + "-"]
    return n1 + n2

def phoqueit(n):
    n1 = []
    n2 = []
    pass

def Fibonacci(n):
    f0 = 0
    f1 = 1
    tup = (f0,f1)
    for i in range(2,n):
        f2 = f1 +f0
        tup += (f2)
        f0 = f1
        f1 = f2
    return tup

print(Fibonacci(10))
#print(factorielle(5))
#print(TrianglePascal(6))
#print(phoque(4))
