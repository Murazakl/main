# ex 1
# fonction vu en cours
def multbyalpha(b,f):
    y = b << 1
    if (y >> (len(bin(f)) - 3)):
        y = y ^ f
    return y

# ex 2
# fonction vu en cours
def multiplication(b,c,f):
    r = 0
    while b != 0:
        if (b & 1) != 0:
            r = r ^ c
        c = multbyalpha(c,f)
        b = b >> 1
    return r

# ex 3
# fonction vu en cours
def table_log(P):
    cardinal = (1 << (len(bin(P)) - 3))
    L = [0] * cardinal
    L[0] = -1
    z = 1
    j = 0
    while j != (cardinal - 1): 
        L[z] = j
        z = multbyalpha(z,P)
        j += 1
    return L

# ex 4
# fonction vu en cours
def table_alpha(P):
    nbr_elements = (1 << (len(bin(P)) - 3)) - 1
    L = [0] * nbr_elements
    L[0] = 1
    alpha = 1
    i = 1
    while i < nbr_elements:
        alpha = multbyalpha(alpha,P)
        L[i] = alpha
        i += 1
    return L

# ex 5
# résultat du produit dans F2m de u par v
def multiplie(x,y,P):
    if x == 0 or y == 0:
        return 0
    return alpha_table[(log_table[x] + log_table[y]) % ((1 << (len(bin(P)) - 3)) - 1)]

# ex 6
# Cette fonction renvoie l'entier z qui représente l'élément Q(u).
def evalue(Q,y,P):
    i = len(Q) - 1
    res = Q[i]
    while i > 0:
        res = multiplie(res,y,P)
        res = res ^ Q[i-1]
        i -= 1
    return res

# ex 7
# Cette fonction renvoie la liste des entiers représentant
# les éléments du sous-groupe de F∗2m généré par l'élément u.
def sous_groupe_gen(b,f):
    L = []
    c = b
    while b != 1:
        L + = [c]
        c = multiplication(b,c,f)
    L += [1]
    return L

# ex 8
# Cette fonction renvoie l'ordre de l'élément u dans F∗2m.
def ordre(b,f):
    return len(sous_groupe_gen(b,f))

# ex 9
# Cette fonction doit renvoyer l'entier z qui représente
# le symétrique pour la loi × de u dans F2m.
def symetrique_mul(x,P):
    return alpha_table[((1 << len(bin(P)[3:])) - 1) - log_table[x]]

# ex 10
# Verifie si c est la symétrie de b avec fonction : multiplication(b,c,f)
def is_sym_mul(b,c,f):
    return multiplication(b,c,f) == 1

# ex 11
# Verifie si c est la symétrie de b avec listes : log_table et alpha_table
def is_sym_mul2(b,c,f):
    return alpha_table[(log_table[b] + log_table[c]) % ((1 << len(bin(f)[3:])) - 1)] == 1

# ex 11 bis
def is_sym_mul2(b,c,f):
    return alpha_table[((1 << len(bin(P)[3:])) - 1) - log_table[b]] == c

# ex 11 bis
def is_sym_mul2(b,c,f):
    return (log_table[b] + log_table[c]) % (len(alpha_table) - 1) == 0
    
print(evalue([4,3,6],2,13))
