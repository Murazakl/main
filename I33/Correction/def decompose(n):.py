def decompose(n):
	if n==0:
		return [0]
	L=[]
    while n != 0 :
        L = [n%2] + L
        n = n // 2
    return L

print(decompose(99999876400))