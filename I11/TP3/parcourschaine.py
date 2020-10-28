from pocketnoobj import *

ch = input("saisir une chaine de caracteres :")
i = 0
while i < len(ch):
    if isalpha(ch[i]) :
        print(ch[i],': caractere')
    elif isdigit(ch[i]) :
        print(ch[i],': chiffre')
    else :
        print(ch[i],': special')  
    i = i + 1
