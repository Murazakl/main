def transpose(M):
    return [[M[j][i] for j in range (len(M))] for i in range (len(M[0]))]

def gensym(n,t):
    M = gentrianginf(n,t)
    for i in range (n):
        for j in range (i+1, n):
            M[i][j] = M[j][i]
    return M
    
def is_symetrique(M):
    if len(M) != len(M[0]):
        return False
    for i in range (len(M)):
        for j in range (i+1, len(M)):
            if M[j][i] != M[i][j]:
                return False
    return True
    
def norme(M):
    som_max = 0
    for j in range (len(M[0])):
        som = 0
        for i in range (len(M)):
            som += abs(M[i][j])
        if som_max < som:
            som_max = som
    return som_max

def matvec(M,V):
    L = [0] * len(M)
    for i in range (len(M)):
        for j in range (len(V)):
            L[i] += M[i][j] * V[j]
    return L
            
def matmat(A,B):
    L = [0] * len(A)
    for i in range (len(A)):
        L[i] = [0] * len(B[0])
        for j in range (len(B[0])):
            for k in range (len(B)):
                L[i][j] += A[i][k] * B[k][j]
    return L

def prod_mat_vec_F2(M,V):
    res = 0
    for i in range (len(M)):
        res <<= 1
        res |= poids(M[i] & V) & 1
    return res

def matmat2(A,B,P):
    L = []
    for i in range (len(A)):
        tmp = []
        for j in range (len(B[0])):
            som = 0
            for k in range (len(A[0])):
                som ^= multiplie(A[i][k],B[k][j],P)
            tmp += [som]
        L += [tmp]
    return L
            

print(matmat([[1,1,2],[1,0,2]],[[1,2,0,1],[1,1,1,0],[0,2,2,1]]))
