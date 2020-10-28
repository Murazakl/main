a = float (input('Entrer une valeur : '))
b = float (input('Entrer une valeur : '))
c = float (input('Entrer une valeur : '))
if a == 0 :

    if b == 0 :

        if c == 0 :
            print ('Infinite de solutions')

        else :
            print ('Pas de solutions')

    else :
        x = -c / b
        print (x)
else :

    d = b**2 + ((-4 * a) * c)

    if d > 0 :
        x1 = (-b + d**(1/2)) / (2*a)
        x2 = (-b - d**(1/2)) / (2*a)
        print (x1 ,x2)

    elif d == 0 :
        x3 = -b / (2*a)
        print (x3)

    else :
        print ('Pas de solutions reelles')
