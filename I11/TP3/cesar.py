chiffre = input('E ou D ? ')
cle = int(input('cle de chiffre ? '))
i = 0
clair = ''
if chiffre == 'E' :
    ch = input('Texte : ')
elif chiffre == 'D' :
    ch = input('Texte : ')
    cle = -cle
while i < len(ch) :
    if ch[i] != ' ' :
        clair += chr(ord(ch[i]) + cle)
    else :
        clair += ' '
    i += 1
print('clair :',clair)
    
