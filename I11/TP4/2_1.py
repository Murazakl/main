a = int(input('Saisir un entier : '))
ma_liste = []
somme = 0
while a != 0 :
    ma_liste = ma_liste + [a]
    somme = somme + a
    a = int(input('Saisir un nouvel entier : '))
print('nombre d entiers :',len(ma_liste),'somme :',somme)
