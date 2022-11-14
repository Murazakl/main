def cardinal(t):
# il suffit ici de compter le nombre
# de 1 dans la decomposition en base
# 2 de t. Il faut donc appliquer
# l'algorithme de decomposition en
# base 2
    cpt = 0
    while t!=0:
        if (t&1)==1:
             cpt += 1
        t = t >> 1
    return cpt

def plus_grand_elem(t):
# ici on decale t de 1 position 
# vers la droite jusqu'a tomber 
# sur 0. Le nombre de decalages
# effectues donne la position
# du bit de poids fort et donc
# la valeur du plus grand element
    val = 0
    while t != 1:
        val += 1
        t = t >> 1
    return val


def plus_petit_elem(t):
# ici on cherche la position du premier 
# 1 dans la representation binaire de t
# donc tant que le bit de poids faible vaut 0
# on decale t d'une position vers la droite
# le nombre de decalage donne la position 
# recherchee
    val = 0
    while (t & 1) == 0:
        val += 1
        t = t >> 1
    return val

def decompose(n):
# cette fonction a ete ecrite a 90% lors du
# precedent TP, il suffisait juste ici de rajouter
# un compteur pour compter le nombre de divisions.
    L = []
    cpt = 0
    while (n % 2) == 0:
        cpt = cpt + 1
        n = n // 2
    if (cpt != 0):
        L += [[2,cpt]]
    i = 3
    while n != 1:
        cpt = 0
        while (n % i) == 0:
            cpt = cpt + 1
            n = n // i
        if (cpt != 0):
            L += [[i,cpt]]
        i = i + 2
    return L

def compose(f,g):
# cf. TD1
    return [f[0]*g[0],f[0]*g[1]+f[1]]

def symetrique(f):
# cf. TD1
    return [1/f[0],-f[1]/f[0]]
