#Desarrollar  una  aplicación  que  posea  una  función  que  reciba  un  arreglo  y  un  valor  y  verifique  si  dicho  valor 
#existe en el arreglo. Para probar su funcionamiento el usuario debe generar un arreglo de tamaño variable que 
#contiene números al azar entre 1 y 50 e indicar el número que desea buscar en el arreglo.

import random 
import msvcrt

try:

    print("============Encontrar números en un arreglo============")

    n=int(input("Ingrese el tamaño de la lista: "))
    k=int(input("Ingrese el número a encontrar en la lista: "))
    
    list=[]

    for i in range (n):
        list.append(random.randint(1,50))

    print(f"La lista es: {list}")

    for i in range (n):
        if list.count(k)>0:
            print(f"El número {k} SI existe en la lista.")
            break
        else:
            print(f"el número {k} NO existe en la lista")
            break
                
    

except:
    print("Usted ha ingresado datos que no son números enteros.")



msvcrt.getch()