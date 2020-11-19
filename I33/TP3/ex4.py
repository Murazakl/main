def multiplie(x,y,P):
    if (x==0 or y==0):
        return 0    
    else:
        taille = len(bin(P)) - 3
        i = log_table[x]
        j = log_table[y]
        z = alpha_table[(i + j) % ((1 << taille) - 1)]
        return z