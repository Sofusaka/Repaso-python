#Desarrollar  un  algoritmo  que  genere  al  azar  N  números  entre  1  y  100.  La  cantidad  N  debe  ser  solicitada  al 
#usuario y los valores deben ser impresos separados por coma. Al finalizar se debe indicar cuál es el mayor y el 
#menor número generado y el promedio de dichos números.

import random 
import msvcrt

print("==============Generador y ordenador de números aleatorios==============")
try:
    n=int(input("Escriba la cantidad de números aleatorios a generar: "))
    list=[]

    for i in range (n):
        
        list.append(random.randint(1,100))
    print(f"Los números generados son:{list} ")
    print("=="*6*n)
    print(f"El número mayor generado es {max(list)}, el número menor generado es {min(list)} y el promedio de los números es {sum(list)/n}")
    


except:
     print("Usted ha ingresado un valor que no es número entero.")


msvcrt.getch()