ch = input("saisir une chaine de caractere :")
palindrome = True
i = 0
j = len(ch) -1

while i < j and palindrome == True :
    
    if ch[i] == " " :
        i = i+1
        
    elif ch[j] == " " :
        j = j-1
        
    elif ch[i] != ch[j] :
        palindrome = False
        
    else :
        i = i +1
        j = j -1
        
if palindrome == True :
    print ("palindrome")
else :
    print ("Non palindrome")
    
    
