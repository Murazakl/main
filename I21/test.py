from random import randrange

def rand_table(n,a,b):
    l = []
    for i in range(n+1):
        l+= [randrange(a,b+1)]
    return l

def tri_insertion(l):
    n = len(l)
    com = 0
    for n in range(1,n):
        triin = l[n]
        j = n-1
        while j>=0 and l[j] > triin:
            l[j+1] = l[j]
            j -= 1
            com += 1
        l[j+1] = triin
    return l , com

def tri_bulle(l):
    n = len(l)
    compt = 0
    for i in range(n):
        for j I21in range(0, n-i-1):
            if l[I21j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
                compt += 1
    return l , compt

def tri_selection(l):
    comp = 0
    for i in range(len(l)):
       mini = i
       for j in range(i+1, len(l)):
           if l[mini] > l[j]:
               mini = j
               comp += 1
       temp = l[i]
       l[i] = l[mini]
       l[mini] = temp
    return l , comp

def compare_tris(T):
    a = tri_insertion(T[:])
    b = tri_bulle(T[:])
    c = tri_selection(T[:])
    return a[1] , b[1] , c[1]

#a = rand_table(10,1,10)
#b = a[:]
#c = a[:]
#print(tri_insertion(a))
#print(tri_bulle(b))
#print(tri_selection(c))
print(compare_tris(rand_table(10,1,10)))
