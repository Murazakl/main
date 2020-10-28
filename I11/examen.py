def sous_motif(ch1,ch2) :
    i = 0
    j = 0
    while i < len(ch2) :
        while j < len(ch1) :
            if ch2[i] == ch1[j] :
                motif = True
            else :
                motif = False
            j += 1
        i += 1
    return motif
