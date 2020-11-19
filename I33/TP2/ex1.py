def pgcd(a,b):
    if b == 0:
        return a
    else :
        r = a % b
        return pgcd(b,r)

print(pgcd(13,21))

#OPTION 2

def pgcd2(a,b):
    while b > 0:
        a, b = b, a % b
    return a