#Leer una cantidad variable conocida de números e indicar finalmente cual fue el mayor número leído y cuantas
#veces fue ingresado.

import msvcrt
try:
    print("=================Valor máximo de números=================")

    list=[]
    cant= int(input("Ingrese la cantidad de números a ingresar: "))
    for i in range (cant):
        num=int(input("Ingrese el número: "))
        list.append(num)

    mayor=max(list)
    print(f"El número mayor de la lista es {mayor}, y se repite {list.count(mayor)} veces")



except:
    print("Usted ha ingresado valores que no son numeros enteros.")


msvcrt.getch()