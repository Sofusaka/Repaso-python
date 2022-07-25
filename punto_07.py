#Desarrollar un algoritmo que llene un arreglo de 20 posiciones con números al azar entre 0 y 10. Posteriormente 
#deberá mover todos los ceros que aparezcan al final del arreglo, manteniendo el orden relativo de los números 
#que no son cero. Se deberá imprimir el arreglo antes y después del cambio.


import random 
import msvcrt

print("============Función para mover todos los ceros presentes en la lista al final============")

list=[]
list0=[]
count=0

for i in range (20):
    list.append(random.randint(0,10))

print(f"La lista inicial es: {list}")
for i in range (len(list)):
    x=list[i]
    if x!=0:
        list0.append(x)
        count+=1

for i in range (count, len(list)):
    list0.append(0)

print(f"La lista con los ceros al final es: {list0}")


msvcrt.getch()