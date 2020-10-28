from pocketgl import *

init_window('premiers pas', 500, 500)

i = 0
j = 0

while i < 510 :
    current_color(j,j,j)
    box(0 ,i ,500 ,i+10)
    i += 10
    j += 5
main_loop()
