lettres = "abcdefghijklmnopqrstuvwz"
parenth = "()"
opera = "!+*"

def ListerVariables(expression):
    varia = []
    for charac in expression:
        if charac in lettres and not charac in varia:
            varia += [charac]
    return sorted(varia)

def DicoVariable(liste):
    divaria = {}
    for i, charac in enumerate(liste):
        divaria[charac] = i
    return divaria

def Int2Bin(entier,n):
    b = bin(entier)[2:]
    ch = ""
    i = n-len(b)
    while i > 0:
        ch += "0"
        i -= 1
    ch += b
    return ch

def Bin2Bool(bits):
    i = 0
    ft = []
    while len(bits) > i:
        if bits[i] == "0":
            ft += [False]
        else :
            ft += [True]
        i += 1
    return tuple(ft)

def Math2Python(expression,vecteur,dico):
    ch2 = ""
    for chara in expression:
        if chara == "!":  ch2 += "not "
        if chara == "+":  ch2 += "or"
        if chara == "*":  ch2 += "and"
        if chara == "(":  ch2 += "("
        if chara == ")":  ch2 += ")"
        if chara == " ":  ch2 += " "
        if chara in dico:
            ch2 += str(vecteur[dico[chara]])
    return ch2

def TableVerite(expression,dico):
    for E in range(0,2**3):
        Bin2Bool(3)



expression = "!(p + q) * (!p + r) + (p * q)"

variables = ListerVariables(expression)
dico = DicoVariables(variables)

print(variables, dico)
print(Int2Bin(5,5))
print(Bin2Bool(Int2Bin(5,5)))

print(Math2Python(expression,(False, False, True),dico))
