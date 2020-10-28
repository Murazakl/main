n = int(input('Entrer une valeur :'))
total = 0
totalp = 0
totali = 0
while n != 0 :

    total = total + n
    verif = n%2

    if verif == 0 :
        totalp = totalp + n

    else :
        totali = totali + n

    n = int(input('Entrer une valeur :'))
print('Somme total :',total)
print('Somme paires :',totalp)
print('Somme impaires :',totali)
