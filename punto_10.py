#Un  BOING  747  tiene  una  capacidad  de  carga  para  equipaje  de  aproximadamente  18.000  kg.  Desarrolle  un 
#algoritmo que controle la recepción de equipajes para este avión, sabiendo: 
#   a. Un bulto no puede exceder la capacidad de carga del avión ni tampoco exceder los 500 Kg. 
#   b. El valor por kilo del bulto es : 
#       - de 0 a 25 Kg. cero pesos 
#       - de 26 a 300 Kg., $1500 pesos por kilo de equipaje. 
#       - de 301 a 500 Kg. $2500 pesos por kilo de equipaje 
 
#Para un vuelo cualquiera se pide: 
#   a. Número total de bultos ingresados para el vuelo 
#   b. Peso del bulto más pesado y del más liviano 
#   c. Peso promedio de los bultos 
#   d. Ingreso en pesos y en dólares por concepto de carga. 
 
#Construya una tabla de seguimiento con no menos de 15 bultos para realizar la prueba del algoritmo.

import msvcrt

def precio(n):
    if n<=25:
        return 0
    if n>26 and n<=300:
        caso1=n*1500
        return caso1
    if n>301 and n<500:
        caso2=n*2500
        return caso2

list=[]
ganancia=0
pr=0

try:
    print("======================Calcular equipaje de un BOING 747======================")

    cbultos=int(input("Digite la cantidad de bultos a cargar: "))


    for i in range(cbultos):

        bulto=int(input(f"Ingrese el peso del bulto {i+1}: "))
        list.append(bulto)

        while sum(list)>1800 or bulto>500:
            print("El bulto no cumple con los requisitos preestablecidos. Ingrese el dato nuevamente.")
            list.remove(bulto)
            bulto=int(input(f"Ingrese el peso del bulto {i+1}: "))

        
        pr=precio(bulto)
        ganancia=ganancia+pr

    print("="*70)

    print(f"\nLa cantidad de bultos ingresados es {cbultos}")
    print(f"El peso del bulto más pesado es {max(list)} kg")
    print(f"El peso del bulto más liviano es {min(list)} kg")
    print(f"El promedio del peso de los bultos es {round(sum(list)/cbultos,2)}kg")
    print(f"El ingreso en pesos es COP ${ganancia}, y en dólares es USD ${round(ganancia/4500,2)}")

except:
    print("Usted ha ingresado un valor bultos que no es un número entero.")


msvcrt.getch()
    

    

