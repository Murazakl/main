ch = input('chaine de caractere : ')
i = 0
ch2 = ''
while i < len(ch) :
    if ord(ch[i]) >= 49 and ord(ch[i]) <= 57 :
        ch2 += ch[i]        
    elif ord(ch[i]) == 32 :
        ch2 += ch[i]
    i += 1
print('Nombres presents:',ch2)
        
        
