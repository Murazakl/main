def decompose(n):
    L = []
    while n != 0:
        L += [n % 2]
        n = n // 2
    return L[::-1]

print(decompose(99999876400))