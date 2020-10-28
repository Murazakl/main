def somme(u,v) :
    for i in range(len(u)) :
        somm += mult(a,u) + mult(b,v)
    return somm

def mult(a,u) :
    for j in range(len(u)) :
        mul = u[j] * a
        mul2 = v[j] * b
        L += [mul]
        L2 += [mul2]
    return L,L2

u = (1,2,1,3)
v = (4,1,0,2)
a = int(input('Saisir un entier : '))
b = int(input('Saisir un entier : '))
somm = 0

mult(a,u)
mult(b,v)
somme(u,v)
print(somm)






