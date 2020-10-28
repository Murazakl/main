L = ["je", "tu"]
mini = L[0]
maxi = L[0]
b = len(mini)
c = len(maxi)
i = 1
while i < len(L) :
    if c < len(L[i]) :
        maxi = L[i]
    elif c > len(L[i]) :
        if b > len(L[i]) :
            mini = L[i]
    i += 1
print('min =',mini)
print('max =',maxi)
