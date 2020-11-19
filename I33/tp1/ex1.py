def somme_pair(L):
    i= 0
    somme = 0
    for i in range (len(L)):
        if L[i] % 2 == 0:
            somme += L[i]
    return somme

L= [3,2,5,7,4,1]
print(somme_pair(L))
