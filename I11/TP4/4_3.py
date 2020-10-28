a = int(input('Saisir une longueur : '))
liste = ['a','bf','c','dg','az']
liste2 = []
i = 0
while i < len(liste) :
    if len(liste[i]) == a :
        liste2 = liste2 + [liste[i]]
    i = i +1
print(liste2)
