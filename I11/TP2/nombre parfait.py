n = int(input('Saisir un entier : '))
i = 1
compt = 0
while i < n :
    if n % i == 0 :
        compt = compt + i     
    i = i+1
if compt == n :
    print('nombre parfait')
else :
    print('nombre pas parfait')
    
