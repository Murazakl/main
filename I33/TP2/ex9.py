def pgcd(a, b):
	if b > 0:
		return pgcd(b, a % b)
	return a

def generateurs(n):
    L = []
    for i in range(n):
        if pgcd(i,n) == 1:
            L += [i]
    return L

print(generateurs(6))