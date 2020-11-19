def eval_poly(P,b):
    i = 0
    j = 0
    while i < len(P)-1:
        j += P[i]
        j *= b
        i += 1
    j += P[i]
    return j

