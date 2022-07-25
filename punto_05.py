#Desarrollar un algoritmo que llene un arreglo de 20 posiciones con números al azar entre 15 y 86. 
#Posteriormente  deberá  ordenar  el  vector  de  manera  descendente  e  imprimir  el  vector  antes  y  después  del 
#ordenamiento.

import random 
import msvcrt

print("==============Generador y ordenador de números aleatorios==============")
try:
   
    list=[]

    for i in range (20):
        
        list.append(random.randint(15,86))
    print(f"Los números generados son:{list} ")
    print(f"La lista es orden descendiente: {sorted(list, reverse=True)}")
    


except:
     print("Ha ocurrido un error inesperado.")



msvcrt.getch()