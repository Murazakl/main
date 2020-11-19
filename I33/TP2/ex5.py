def decompose(n,b):
    L = []
    while n != 0:
        L += [n % b]
        n = n // b
    return L[::-1]

print(decompose(30, 5))