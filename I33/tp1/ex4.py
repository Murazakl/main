def som_div_propres(n):
    i = 2
    somme = 1
    if n == 1:
        return 0
    while i <= n**(1/2):
        if n % i == 0:
            somme += i
            if n/i != i:
                somme += n/i
        i += 1
    return int(somme)

n = 64
print(som_div_propres(n))