import math
import random
#Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.

#1)
#Crear una lista con las notas de 10 estudiantes.
#● Mostrar la lista completa.
#● Calcular y mostrar el promedio.
#● Indicar la nota más alta y la más baja.

"""
listaNotas = [6,8,9,1,7,8,3,2,9,8]
promedio = 0
acumuladorPromedio = 0
notaMasBaja = 0
notaMasAlta = 0
bandera = True

for elemento in range(len(listaNotas)) : 

    acumuladorPromedio += listaNotas[elemento]
    print(f"Estudiante Nota : {listaNotas[elemento]}" ) 

    if bandera == True :
        bandera = False
        notaMasBaja = listaNotas[elemento]
        notaMasAlta = listaNotas[elemento]

    if notaMasAlta < listaNotas[elemento] :
        notaMasAlta = listaNotas[elemento] 
    
    if notaMasBaja > listaNotas[elemento] :
        notaMasBaja = listaNotas[elemento]


promedio = acumuladorPromedio/len(listaNotas)

print(f"Promedio : {promedio}")
print(f"Nota mas alta : {notaMasAlta}")
print(f"Nota mas baja : {notaMasBaja}")

"""

#2) Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.

listaProductos = []
producto = ""
listaOrdenada = []
eliminar = -1

for indice in range(5):

    producto = input(f"Ingrese nombre del producto ->({indice}) : ")
    listaProductos.append(producto)#cargamos el producto

listaOrdenada = sorted(listaProductos)

for indice in range(len(listaOrdenada)) :
    print(f"Producto : {listaOrdenada[indice]} indice -> {indice}" ) 

print("Para eliminar un producto ingrese su indice ")
eliminar = input("Ingrese indice a eliminar : ")

while not eliminar.isdigit() :
    
    print("Para eliminar un producto ingrese su indice ")
    eliminar = input("Ingrese indice a eliminar : ")
    eliminar = int(eliminar)

eliminar = int(eliminar)

del listaOrdenada[eliminar]


for indice in range(len(listaOrdenada)) :
    print(f"Producto : {listaOrdenada[indice]} indice -> {indice}" ) 


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuántos números tiene cada lista.

"""
listaNumeros = []
listaNumerosPares = []
listaNumerosImpares = []

for indice in range(15) :

    listaNumeros.append(random.randint(1,100))

for indice in range(len(listaNumeros)) :

    if listaNumeros[indice] % 2 == 0 :
        #es par
        listaNumerosPares.append(listaNumeros[indice])
    else :
        #es impar
        listaNumerosImpares.append(listaNumeros[indice])

print("LISTA NUMEROS :")

for indice in range(len(listaNumeros)) :
    print(listaNumeros[indice])

print("LISTA NUMEROS PARES")
for indice in range(len(listaNumerosPares)) :
    print(listaNumerosPares[indice])

print("LISTA NUMEROS IMPARES")
for indice in range(len(listaNumerosImpares)) :
    print(listaNumerosImpares[indice])

"""
#4) Dada una lista con valores repetidos:[1,3,5,3,7,1,9,5,3]
#● Crear una nueva lista sin elementos repetidos.
#● Mostrar el resultado
datos = [1,3,5,3,7,1,9,5,3]
lista_sinRepetir = []

for elemento in datos:
    if elemento not in lista_sinRepetir:
        lista_sinRepetir.append(elemento)

print(lista_sinRepetir)
"""
#5)Crear una lista con los nombres de 8 estudiantes presentes en clase.
#● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#● Mostrar la lista final actualizada


# Lista inicial
estudiantes = ["Ana", "Juan", "Pedro", "Lucia", "Maria", "Carlos", "Sofia", "Diego"]

print("Lista actual:", estudiantes)

# Preguntar acción
opcion = input("¿Querés agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

# AGREGAR
if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print("Estudiante agregado.")

# ELIMINAR
elif opcion == "eliminar":
    eliminar = input("Ingrese el nombre a eliminar: ")
    
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("Estudiante eliminado.")
    else:
        print("Ese estudiante no está en la lista.")

else:
    print("Opción inválida.")

# Resultado final
print("Lista final:", estudiantes)




#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
#(el último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo = numeros[-1]  # guardo el último

for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]

numeros[0] = ultimo

print(numeros)


#7)Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
temperaturas = [
    [10, 20],
    [12, 22],
    [9, 18],
    [11, 21],
    [13, 25],
    [8, 17],
    [10, 19]
]

suma_min = 0
suma_max = 0

mayor_amplitud = -1
dia_mayor = 0

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]

    suma_min += minima
    suma_max += maxima

    amplitud = maxima - minima

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1  # +1 para que sea día 1..7

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print(f"Promedio mínimas: {promedio_min:.2f}")
print(f"Promedio máximas: {promedio_max:.2f}")
print(f"Mayor amplitud térmica en el día: {dia_mayor}")





#8)Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia.

# Matriz: 5 estudiantes x 3 materias
notas = [
    [7, 8, 6],
    [9, 7, 8],
    [6, 5, 7],
    [8, 9, 10],
    [4, 6, 5]
]

# Promedio de cada estudiante
print("Promedio por estudiante:")
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    promedio = suma / len(notas[i])
    print(f"Estudiante {i+1}: {promedio:.2f}")

# Promedio de cada materia
print("\nPromedio por materia:")
for j in range(len(notas[0])):  # columnas
    suma = 0
    for i in range(len(notas)):  # filas
        suma += notas[i][j]
    promedio = suma / len(notas)
    print(f"Materia {j+1}: {promedio:.2f}")




#9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializarlo con guiones "-" representando casillas vacías.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.

# Crear tablero 3x3 inicializado con "-"
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Función para mostrar el tablero
def mostrar_tablero(tab):
    for fila in tab:
        print(" ".join(fila))
    print()

# Juego
turno = "X"
jugadas = 0

while jugadas < 9:
    mostrar_tablero(tablero)

    fila = input(f"Jugador {turno} - Ingrese fila (0-2): ")
    while not fila.isdigit() or int(fila) < 0 or int(fila) > 2:
        print("Error.")
        fila = input("Fila (0-2): ")
    fila = int(fila)

    columna = input(f"Jugador {turno} - Ingrese columna (0-2): ")
    while not columna.isdigit() or int(columna) < 0 or int(columna) > 2:
        print("Error.")
        columna = input("Columna (0-2): ")
    columna = int(columna)

    # Verificar si está libre
    if tablero[fila][columna] != "-":
        print("Esa posición ya está ocupada.")
        continue

    # Colocar ficha
    tablero[fila][columna] = turno
    jugadas += 1

    # Cambiar turno
    if turno == "X":
        turno = "O"
    else:
        turno = "X"

# Mostrar tablero final
mostrar_tablero(tablero)
print("Fin del juego.")


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana.
# Matriz 4x7 (4 productos x 7 días)
ventas = [
    [10, 20, 15, 30, 25, 10, 5],   # Producto 1
    [5, 10, 20, 10, 15, 25, 30],   # Producto 2
    [8, 12, 18, 22, 16, 14, 10],   # Producto 3
    [20, 15, 10, 5, 8, 12, 18]     # Producto 4
]

# 1) Total por producto
print("Total vendido por producto:")
totales_producto = []

for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]
    totales_producto.append(total)
    print(f"Producto {i+1}: {total}")

# 2) Día con mayores ventas totales
mayor_ventas = -1
dia_mayor = 0

for j in range(len(ventas[0])):  # recorrer días (columnas)
    total_dia = 0
    for i in range(len(ventas)):  # recorrer productos (filas)
        total_dia += ventas[i][j]

    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j + 1

print(f"\nDía con mayores ventas: Día {dia_mayor} con {mayor_ventas}")

# 3) Producto más vendido en la semana
max_total = -1
producto_mas_vendido = 0

for i in range(len(totales_producto)):
    if totales_producto[i] > max_total:
        max_total = totales_producto[i]
        producto_mas_vendido = i + 1

print(f"\nProducto más vendido: Producto {producto_mas_vendido} con {max_total}")


#11) Crear una lista con los nombres de 10 estudiantes.
# Solicitar al usuario que ingrese un nombre a buscar.
# Indicar si el nombre se encuentra en la lista.
# Mostrar la posición en la que aparece.
# Si no se encuentra, informar que no está en la lista.


# Lista de 10 estudiantes
estudiantes = [
    "Ana", "Juan", "Pedro", "Lucia", "Maria",
    "Carlos", "Sofia", "Diego", "Valeria", "Martin"
]

# Pedir nombre a buscar
buscado = input("Ingrese el nombre a buscar: ").strip().lower()

# Normalizar lista para comparar sin problemas de mayúsculas
estudiantes_norm = [e.lower() for e in estudiantes]

# Buscar
if buscado in estudiantes_norm:
    # Si puede repetirse, mostramos todas las posiciones
    posiciones = []
    for i in range(len(estudiantes_norm)):
        if estudiantes_norm[i] == buscado:
            posiciones.append(i)

    print("El nombre se encuentra en la lista.")
    # +1 si querés mostrar posición humana (1..10)
    print("Posición(es):", [p + 1 for p in posiciones])
else:
    print("El nombre no está en la lista.")





#12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
# Mostrar la lista original.
# Mostrar la lista ordenada de menor a mayor.
# Mostrar la lista ordenada de mayor a menor.
# Investigar el uso de sorted() y del parámetro reverse.
# Pedir 8 números
numeros = []

for i in range(8):
    n = input(f"Ingrese número {i+1}: ")
    while not n.isdigit():
        print("Error: ingrese un número entero.")
        n = input(f"Ingrese número {i+1}: ")
    numeros.append(int(n))

# Mostrar lista original
print("Lista original:", numeros)

# Ordenada de menor a mayor (sin modificar la original)
orden_asc = sorted(numeros)
print("Ordenada de menor a mayor:", orden_asc)

# Ordenada de mayor a menor
orden_desc = sorted(numeros, reverse=True)
print("Ordenada de mayor a menor:", orden_desc)


#Dada la siguiente lista de puntajes de un videojuego:
#puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# Mostrar el puntaje más alto y el más bajo.
# Mostrar la lista ordenada de mayor a menor (ranking).
# Indicar en qué posición del ranking se encuentra el puntaje 990

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Puntaje más alto y más bajo
print("Más alto:", max(puntajes))
print("Más bajo:", min(puntajes))

# Ranking (de mayor a menor)
ranking = sorted(puntajes, reverse=True)
print("Ranking:", ranking)

# Posición del 990 en el ranking (1-based)
if 990 in ranking:
    posicion = ranking.index(990) + 1
    print("El puntaje 990 está en la posición:", posicion)
else:
    print("El puntaje 990 no está en la lista.")
"""