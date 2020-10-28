arthur = True
while arthur :
    a = int (input('Entrer a : '))
    op = input('Entrer op : ')
    b = int (input('Entrer b : '))
    if op == '+' :
        result = a + b
    
    elif op == '-' :
        result = a - b

    elif op == '*' :
        result = a * b

    else :
        result = a / b

    c = type(result)
    print('Valeur de a :',a)
    print('Valeur de b :',b)
    print("Choix d'operateur parmi (+,-,*,/) :",op)
    print('Le resultat est', a,op,b,'=',result)
    print('Cette expression est de type',c)

    rep = input('Continu?(y/n) :')
    if rep == 'n' :
        arthur = False
        
    
