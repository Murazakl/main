def is_LU(A,L,U):
    n = len(A)
    # on verifie que L est triangulaire inferieure
    # si on trouve un element non nul au dessus de la diagonale
    # on s'arrete
    for i in range(n):
        for j in range(i+1,n):
            if L[i][j] != 0:
                return False
    # on verifie que U est triangulaire superieure
    # si on trouve un element non nul au dessous de la diagonale
    # on s'arrete
    for i in range(n):
        for j in range(i):
            if U[i][j] != 0:
                return False
    # enfin on verifie que A = LU
    # que l'on trouve un element A_ij 
    # different de LU_ij on s'arrete
    # ici il suffisait de reprendre le code 
    # de matmat (TP6 Question 7)
    for i in range(n):
        for j in range(n):
            somme = 0
            for k in range(n):
                somme = somme + L[i][k] * U[k][j]
            if somme != A[i][j]:
                return False
    return True

# Pour la question2, certains ont eu a calculer le determinant de A a partir de L et U
# et d'autres devaient verifier que a etait inversible en ayant L et U
# Etant donne que A = LU alors (cf. cours) det(A)=det(L)xdet(U)
# le calcul du determinant de A revenait donc a faire le produit des elements diagonaux de L
# et de U
def determinant(L,U):
    n = len(L)
    prod = 1
    for i in range(n):
        prod = prod * L[i][i] * U[i][i]
    return prod

# Puisque det(A)=det(L)xdet(U) A n'est pas inversible que l'on trouve 
# sur la diagonale de L ou la diagonale de U un element qui vaut 0
def est_inversible(L,U):
    n = len(L)
    inv_ok = True
    i = 0
    while (i < n) and inv_ok:
        inv_ok = (L[i][i] != 0) and (U[i][i] != 0)
        i = i + 1
    return inv_ok

def transpose_LU(L,U):
    # ici on se sert de la formule vue en cours
    # transpose(LU) = transpose(U) x transpose(L)
    # il fallait donc juste reprendre le code 
    # de matmat et l'appliquer Ã  la tranposee de  U
    # et la transposee de L 
    # inutile de calculer ces 2 transposes. En effet
    # l'element en position (i,k) de la transposee de U
    # est l'element en position (k,i) dans U
    # de meme l'element en position (k,j) dans la transposee de L
    # est l'element en position (j,k) dans L
    A_t = []
    n = len(L)
    for i in range(n):
        aux = []
        for j in range(n):
            somme = 0
            for k in range(n):
                somme += U[k][i]*L[j][k]
            aux += [somme]
        A_t += [aux]
    return A_t


def resolution(L,U,b):
# c'etait l'exercice "difficile" mais je rappelle 
# que lors du dernier cours, j'ai fortement insiste
# sur le fait qu'il serait bien pour vous de le 
# programmer. Les 3 exercices precedents prenant au
# maximum 30 minutes, il restait 1h pour traiter
# celui-ci
# On commence par resoudre Ly = b
	y = [b[0]/L[0][0]]
	n = len(L)
	for i in  range(1,n):
		somme = b[i]
		for j in range(i):
			somme = somme - L[i][j]*y[j]
		y = y + [somme/L[i][i]]
# puis on resoud Ux = y
	x = [0]*n
	x[-1] = y[-1]/U[-1][-1]
	i = n - 2
	while i >= 0 :
		somme = y[i]
		for j in range(i+1,n):
			somme = somme - U[i][j]*x[j]
		x[i] = somme/U[i][i]
		i = i-1
	return x
