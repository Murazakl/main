n = int(input('Saisir un entier n : '))
uv = 0
somu = 0
somv = 0
i = 0
while i < n :
    u = float(input('Saisir une valeur de u : '))
    v = float(input('Saisir une valeur de v : '))
    uv += u * v
    somu += (u)**2
    somv += (v)**2
    i += 1
fois = ((somu)**(1/2))*((somv)**(1/2))
cos = uv/fois
print('cosinus de l angle :',cos)
