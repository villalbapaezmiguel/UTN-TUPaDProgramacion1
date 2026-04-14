#desarrollar un algoritmo que nos permita ingresar un numero entero positivo. La 
#computadora debe mostrar la sucesion de numeros pares desde el numero ingresado 
#hasta el cero (inclusive), en una sola linea 
"""

numero = int(input("Ingrese un numero positivo : ")) 
print(f"Ingreso el numero {numero}")
if(numero > 0 ):
    for i in range(numero + 1) :
        if( i % 2 == 0):
            print(f"{i}" , end=" , ") #end="" (para que se pueda mostrar en una sola linea)

else :
    print("ERROR , el numero ingrsado no es positvo...")
"""


#desarrollar un algoritmo que permita ingresar un numero entero entre 1 y 10 (inclusive) . La
#computadora debe mostrar la tabla de multiplicar del numero ingresado

"""
numero = int(input("Ingrese numero (entre 1 y 10) :"))

if numero >=1 and numero <= 10 :
    for i in range(1,11) :
        print(f"{numero} x {i} = {numero*i}")

else :
    print("ERROR , el numeor numero ingresado es incorrecto..")
"""

#desarrollar un algoritmo que nos permita ingresar una cantidad de personas , La computadora debe
#pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad

cantidadPersonas = int(input("Ingrese la cantidad personas : "))
contadorEdadMayor = 0
porcentaje = 0
edad = 0

for i in range(1,cantidadPersonas+1) :
    
    edad = int(input("Ingrese edad : "))

    if edad != 0 and edad >= 18:
        contadorEdadMayor += 1


porcentaje = (contadorEdadMayor / cantidadPersonas)*100

print(f"El porcentaje de personas mayores de {porcentaje}%")
