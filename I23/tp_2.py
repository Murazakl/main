def Lecture(nomfichier):
    with open("liste.txt","r") as fichier:
        X, G, Y = set(), dict(), set()
        for E in fichier.readlines():
            compo = E.rstrip().split(">")
            if not compo[0] in G.keys():
                G[compo[0]] = set()
            X.add(compo[0])
            G[compo[0]].add(compo[1])
            Y.add(compo[1])
        return X, G, Y

def Reciproque(C):
    cle = dict()
    for exit in C[2]:
        if not exit in cle.keys():
            cle[exit] = set()
        for entry in C[0]:
            if exit in C[1][entry]:
                cle[exit].add(entry)
    return C[2], cle, C[0]

def ImageDirecte(C,A):
    imadir = []
    for i in A:
        if A.keys() in C[1] :
            imadir+= C[1][i]
    return imadir

def ImageReciproque(C,B):
    pass

def Composer(g,f):
    pass

def Affiche(c):
    print("X = ",str(c[0]).replace("'",''))
    print("G = ",str(c[1]).replace("'",''))
    print("Y = ",str(c[2]).replace("'",''),end='\n\n')

#Affiche(Lecture("liste.txt"))
#print("Reciproque :")
#Affiche(Reciproque(Lecture("liste.txt")))
print("Image Directe : ", ImageDirecte(Lecture("liste.txt"),))
