semaine = [ " lundi " ," mardi " ," mercredi " ," jeudi " ," vendredi " ," samedi " , " dimanche " ]
calendOct18 = []
date = ""
j = 1
i = 0
while j <= 31 :
    date = semaine[i]+str(j)+' octobre'
    if j%7 != 0 :
        calendOct18 = calendOct18 + [date]
        i = i + 1
    else :
        calendOct18 = calendOct18 + [date]
        i = 0
    j = j + 1
print(calendOct18)
    
