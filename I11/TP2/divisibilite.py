def chiant(n) :
    for i in range(n+1) :
        somme += int(n[i])
        n = str(somme)
        return(somme)

n = input('Sasir un entier positif : ')
i = 0
somme = 0
chiant(n)
while somme < 10 :
    if somme == 3 or somme == 6 or somme == 9 :
        print('divisible par 3')
    else :
        print('non divisible par 3')
    chiant(n)

    


  

    
