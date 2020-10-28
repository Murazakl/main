liste = ['je','m appelle','Yohan','eschberger','buenisnochesmmkezazf']
liste1 = []
liste2 = []
i = 0
while i < len(liste) :
    if len(liste[i]) < 5 :
        liste1 = liste1 + [liste[i]]
    elif len(liste[i]) > 10 :
        liste2 = liste2 + [liste[i]]
    i = i +1
print(liste)
print(liste1)
print(liste2)

