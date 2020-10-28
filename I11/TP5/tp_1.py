def som_div_propres(n,m) : 
    som = 0
    i = 1
    while i < n :
        if n % i == 0 :
            som = som +i
        i = i +1
    return som

def amicaux(n,m) :
    return n == som_div_propres(m) and m == som_div_propres(n)

def affiche_amicaux(k) :
    p = 2**k
    n = 1
    while n < p :
        m = som_div_propres(n)
        if som_div_propres(m) == n :
            print(n,m)
        n = n +1
        


k = int(input('Valeur de k : '))

affiche_amicaux(k)

            






    
