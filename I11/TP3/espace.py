from pocketnoobj import *

ch = input("saisir une chaine de caractere :")
compt = 0
i = 0
while i < len(ch) :
    if ch[i] == " " :
        compt = compt + 1
    i = i + 1
print ('nombre d\'espace :',compt)
