#Leer una cantidad variable de números e indicar cuanto suman todos los números, cuanto los números positivos
#y cuanto los números negativos.

import msvcrt

try:
    print("=============Sumatoria total de numeros enteros=============")

    cant=int(input("Ingrese la cantidad de números que quiere calcular su suma: "))

    sum=0
    sumpos=0
    sumneg=0

    for i in range (0, cant, 1):
        
        sum1=int(input("Ingrese un número: "))
        sum=sum+sum1
        if sum1>=0:
            sumpos=sumpos+sum1
        if sum1<0:
            sumneg=sumneg+sum1

    print (f"La suma total de los números es {sum}, la suma total de los positivos es {sumpos} y la suma total de los negativos es {sumneg}")

except:
    print("Usted ha ingresado valores que no son números enteros.")
msvcrt.getch()