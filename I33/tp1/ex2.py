def minimum(L):
    i = 1
    mini = L[0]
    while i < len(L):
        if mini > L[i]:
            mini = L[i]
        i += 1
    return mini

L= [3,2,5,7,2]
print(minimum(L))