ch = input('chaine de caractere : ')
i = 0
comptnum = 0
comptmot = 0
ch2 = ''
while i < len(ch) :
    if ch[i] != ' ' :       
        i += 1
    else :
        if 49 <= ord(ch[i-1]) <= 57 :
            comptnum += 1
        elif 97 <= ord(ch[i-1]) <= 122 :
            comptmot += 1
        i += 1
print(comptnum,comptmot)

           
        
    
        
