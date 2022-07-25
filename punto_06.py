#Desarrollar un algoritmo que llene dos arreglos A y B de 10 posiciones con números al azar entre 200 y 1000. 
#Posteriormente imprimir cada uno de los vectores y reemplazar los valores de A únicamente con los números 
#pares encontrados en B y reemplazar en B únicamente con los números impares encontrados en A.

import random 
import msvcrt

A=[]
B=[]
Apar=[]
Bimpar=[]

for i in range (10):
            A.append(random.randint(200,1000))
            B.append(random.randint(200,1000))

print(f"La lista A es {A} y la lista B es {B}")


for i in range (10):
            x=B[i]
            if x%2==0:
                Apar.append(x)
            
            y=A[i]
            if y%2!=0:
                Bimpar.append(y)
        
        
        
print(f"La lista A es {Apar} y la lista B es {Bimpar}")


msvcrt.getch()
