import math
# Perimetre et aire d'un cercle

R = float (input("Saisir la valeur du Rayon= "))
P = 2*math.pi*R
A = math.pi*R**2
print ("Perimetre =",P,"Aire =",A)


# Aire d'un triangle (formule de Heron)

a = float (input("Saisir la longueur du premier cote= "))
b = float (input("Saisir la longueur du deuxieme cote= "))
c = float (input("Saisir la longueur du troisieme cote= "))
p = a + b + c
s = (1/2)*p
A = (s*(s-a)*(s-b)*(s-c))**(1/2)
print ("Aire= ",A)


# Conversion de degre Celsius en degre Fahrenheit

C = float (input("Saisir la temperature en degre Celsius= "))
F = (C*(9/5))+32
print ("Temperature en degre farenheit=",F)


# Conversion d'un nombre de seconde en heures/min/sec

S = int (input("Saisir un nombre de secondes= "))
s = S%60
mi = S//60
m = mi%60
h = mi//60
print (h,"h",m,"m",s,"s")

