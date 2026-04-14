import math

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombreIngresado = input("Ingrese nombre : ")
print(f"Hola {nombreIngresado}!")



#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla


nombre = input("Ingrese su nombre : ")
apellido = input("Ingrese su apellido : ")
edad = int(input("Ingrese su edad : "))
residencia = input("Ingrese su residencia : ")

print(f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {residencia }.")




#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio de un circulo : "))

area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio

print(f"Area = {area} | Perimetro = {perimetro}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale

segundosIngresado = int(input("Ingrese segundos : "))

horas = segundosIngresado / 3600

print(f"Los {segundosIngresado} equivalen a : {horas} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un numero : "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numeroUno = int(input("Ingrese primer numero (dintinto de cero): "))
numeroDos = int(input("Ingrese segundo numero (dintinto de cero): "))

if((numeroUno != 0) and numeroDos != 0) : 

    print(f"{numeroUno} + {numeroDos} = {numeroUno + numeroDos}")
    print(f"{numeroUno} - {numeroDos} = {numeroUno - numeroDos}")
    print(f"{numeroUno} * {numeroDos} = {numeroUno * numeroDos}")
    print(f"{numeroUno} / {numeroDos} = {numeroUno // numeroDos}")

else : 
    print("ERROR Ingresaste en uno de los numeros un cero...")



#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo

altura = float(input("Ingrese altura : "))
peso = float(input("Ingrese peso : "))

imc = peso / (altura ** 2)

print(f"Su masa corponral es : {imc}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingrese temperatura en Celsius : "))
fahrenheit = 9//5 * celsius + 32

print(f"temperatura en Celsius ingresada : {celsius}")
print(f"Equivalencia en grados Fahrenheit : {fahrenheit}")


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numeroUno = int(input("Ingrese el primer numero : "))
numeroDos = int(input("Ingrese el segundo numero : "))
numeroTres = int(input("Ingrese el tercer numero : "))

promedio = (numeroUno + numeroDos + numeroTres) / 3

print(f"El promedio es : {promedio}")