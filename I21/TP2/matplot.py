import matplotlib.pyplot as plt
from math import cos,sin,pi
# On cree la liste des abscisses des point que l ’ on veut tracer
"""abscisse = []
for i in range(10):
    abscisse += [ i ]
# On cree la liste des ordonnees des points que l ’ on veut tracer :
carre = []
for i in range( len ( abscisse )):
    carre += [ abscisse [ i ]**2]
cube = []
for i in range ( len ( abscisse )):
    cube += [ abscisse [ i ]**3]
# plot () trace les courbes correspondantes et show () les affiche
# a l ’ ecran .
plt.plot( abscisse , carre , abscisse , cube )
plt.show()

def intervalle(a,b,inc):
    t= []
    while a <= b:
        t+= [a]
        a+= inc
    return t

def valeur_sin(t):
    s= []
    for i in range(len(t)):
        s+= [sin(t[i])]
    return s

def valeur_cos(t):
    c= []
    for i in range(len(t)):
        c+= [cos(t[i])]
    return c


absin= intervalle(-2*pi,2*pi,0.2)
abcos= intervalle(-2*pi,2*pi,0.2)

carsin= []
for i in range(len(absin)):
    carsin+= [absin[i]**2]
carcos= []
for i in range(len(abcos)):
    carcos+= [abcos[i]**2]

cubsin= []
for i in range (len(absin)):
    cubsin+= [absin[i]**3]
cubcos= []
for i in range(len(abcos)):
    cubcos+= [abcos[i]**3]

plt.plot(absin, carsin)
plt.show()"""

def multiplication(n1,n2):
    j= 0
    while j <= len(n2):
        i,r = 0,0
        while i <= len(n1):
            p= n3[i+j] + n1[i]*n2[j]+r
            n3[i+j]= (pmod(10))
            r= [p/10]
            i+= 1
        n3[i+j]= r
        j+= 1
    return n3


from  time  import  time
from  random  import  randrange

def time_mukt_py(n,k):
    lim= 10**20
    l= []
    for i in range(k):
        n1= randrange(lim)
        n2= randrange(lim)
        l+= [(n1,n2)]
    start=time()
    for n1,n2 in l:
        n3= n1*n2
    end=time()
    print(end-start)


time_mukt_py(20,10000)




"""print(intervalle(0,1,0.2))
t= intervalle(0,1,0.2)
print(valeur_sin(t))
print(valeur_cos(t))"""
