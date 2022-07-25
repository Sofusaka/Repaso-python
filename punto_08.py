 #Desarrollar un algoritmo que imprima el siguiente patrón utilizando un arreglo bidimensional: 
#- - - - o - - - - 
#- - - - o - - - - 
#- - - - o - - - - 
#- - - - o - - - - 
#o o o o o o o o o 
#- - - - o - - - - 
#- - - - o - - - - 
#- - - - o - - - - 
#- - - - o - - - - 

import msvcrt

print("============Figuras en Python============")
print("")
max = 9
fig = [[ False for x in range(max)]
                for y in range(max)]
 
for a in range(9) :
        for l in range(9) :
            fig[a][l] = '-'

for a in range(9):
    fig[a][4]='o'

for a in range (9):
    fig[4][a]='o'

for a in range (9):
    for l in range (9):
        print(fig[l][a], end='  ')
    print()


msvcrt.getch()

