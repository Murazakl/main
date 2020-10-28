# Pour un TP commencant a 13H00

a = input('Entrer une heure : ')
b = int(a[:2])
c = int(a[3:])
if b < 13 :
    print ('Vous etes en avance')
elif b == 13 :
    if c == 0 :
        print ('Vous etes a l heure')
    else :
        print ('Vous etes en retard')
else :
    print ('Vous etes en retard')


