def minimum2(L):
    mini = L[0]
    i = 1
    while i < len(L):
        if mini > L[i]:
            mini = L[i]
        i += 1

    i = 0
    while L[i] == mini:
        i += 1
    mini2 = L[i]
    i = 0
    while i < len(L):
        if L[i] != mini and mini2 > L[i]:
            mini2 = L[i]
        i += 1
    return mini2
