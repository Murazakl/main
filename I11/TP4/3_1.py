ma_liste = [60,-1,52102,666,-54,12003]
i = 1
maxi = ma_liste[0]
maxi2 = 0
indice = 0
indice2 = 0
while i < len(ma_liste) :
    if maxi < ma_liste[i] :        
        maxi2 = maxi
        maxi = ma_liste[i]
        indice = i
    elif maxi2 < ma_liste[i] :
        maxi2 = ma_liste[i]
        indice2 = i
    i = i +1
print(maxi,'indice :',indice,maxi2,'indice :',indice2)
