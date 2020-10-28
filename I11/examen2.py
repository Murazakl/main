def som_div_propres(n) : 
    som = 0
    i = 1
    while i < n :
        if n % i == 0 :
            som += i
        i += 1
    return som

def est_sophie_germain(n) :
    if som_div_propres(n) == 1 :
        if som_div_propres((2*n)+1) == 1 :
            sophie = True
        elif som_div_propres((2*n)+1) != 1 :
            sophie = False
    return sophie


    
    
    


    
    
