from pocketnoobj import *

ch = input("saisir une chaine de caractere :")
ch2 = ""
i = 0
while i < len(ch) :
    if isalpha(ch[i]) :
        ch2 = ch2 + ch[i]
    elif isdigit(ch[i]) :
        ch2 = ch2 + ch[i]
    i = i + 1
print (ch2)
