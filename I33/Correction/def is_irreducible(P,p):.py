def is_irreducible(P,p):
	_irr = True
    b = 0
    while (b < p) and _irr: 
        val=P[0]
        for i in range(1,len(P)):
            val = (val*b + P[i]) % p 
        _irr = (val != 0)
        b = b + 1
    return _irr
    
print(is_irreducible(6,3)))