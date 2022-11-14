def is_sym_add(x,y,n):
# definition du symetrique de x dans (Z/nZ,+)
# c'est l'element y qui verifie x+y = 0 modulo n
	return ((x+y)%n == 0)
	
def is_sym_mul(x,y,n):
# definition du symetrique de x dans (Z/nZ)*
# c'est l'element y qui verifie x*y = 1 modulo n
	return ((x*y)%n == 1)
	
def is_sym_add(x,y):
# definition du symetrique de x=a/b dans (Q,+)
# c'est l'element y=c/d qui verifie x+y = 0 
# c'est a dire a/b + c/d = 0
# c'est a dire (a*d+b*c)/bd = 0
# c'est a dire (a*d+b*c) = 0
	return (x[0]*y[1]+y[0]*x[1]) == 0
	
def is_sym_mul(x,y):
# definition du symetrique de x=a/b dans (Q,x)
# c'est l'element y=c/d qui verifie x*y = 1 
# c'est a dire (a/b)*(c/d)=1
# c'est a dire (a*c)/(b*d) = 1
# c'est a dire a*c = b*d 
	return (x[0]*y[0]) == (x[1]*y[1])	

def is_of_order(a,t,n):
# cf question 1 , exercice 3, TD1
	return t==(n//pgcd(a,n))
	

def is_of_order_mult(a,t,n):
# c'etait le seul exercice difficile
# je vous laisse y reflechir
# la solution s'inspire de som_div_propres fait
# au TP1
        oncontinue = (pow(a,t,n) == 1) and (a != 1)
        j = 2
        while j*j <= t and oncontinue:
            if (t % j)==0:
                oncontinue = ((pow(a,j,n) != 1) and (pow(a,t//j,n) != 1))
            j = j + 1
        return oncontinue or ((a==1) and (t==1))

