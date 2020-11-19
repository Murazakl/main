def tri_selection(L):
    for i in range(len(L)):
        mini = i
        for j in range(i+1, len(L)):
            if L[mini] > L[j]:
               mini = j
                
        tmp = L[i]
        L[i] = L[mini]
        L[mini] = tmp
    return L

L = [98, 22, 15, 32, 2, 74, 63, 70]
 
print(tri_selection(L))