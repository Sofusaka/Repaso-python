#Desarrolle  un  algoritmo  que  imprima  los  primeros  N  números  primos.  La  cantidad  N  debe  ser  solicitada  al 
#usuario y los valores deben ser impresos separados por coma.

import msvcrt

def primos(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True

    
print("=================Calculadora de números primos=================")
try:
    N=int(input("Ingrese la cantidad de números primos que quiere imprimir: "))

    primoslist=[]
    i=2
    if N>1:

        while True:
            if (primos(i)):
                    primoslist.append(i)
                    if(len(primoslist)==N): 
                        break 
            i=i+1
            
        print(f"los primeros {N} números primos son : {primoslist}")

except:
    print("Usted ha ingresado un valor que no es número entero.")
    

msvcrt.getch()
        

            