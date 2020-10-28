from random import randrange
from pocketgl import *

L = [0,0,0,0,0,0]
L2 = [0,0,0,0,0,0]
L3 = [0,0,0,0,0,0,0,0,0,0,0,0]
i = 0

while i < 10000 :
    de1 = randrange(1,7)
    de2 = randrange(1,7)
    compt = de1 + de2
    L[de1-1] += 1
    L2[de2-1] += 1
    L3[compt-1] += 1
    i += 1

j = 0
k = 0
init_window('histogramme',500,500)
current_color(0,0,255)
box(0,k,10,k+10)
    k += 5
    j += 1
main_loop()
