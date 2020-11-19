def tri_bulle(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1] :
                L[j], L[j+1] = L[j+1], L[j]
    return L

L = [98, 22, 15, 32, 2, 74, 63, 70] 
print(tri_bulle(L))