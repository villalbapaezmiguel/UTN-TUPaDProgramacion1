#variables : 
nombreCliente = 0
cantidadProductos = 0
precioIngresado = 0
acumuladorPrecio_ConDescuento = 0
acumuladorPrecio_SinDescuento = 0
precioFinal = 0
informacion = ""
ahorro = 0
promedio = 0.0

print("##################################### CAJA DE KIOSCO #####################################")


#validamos el nombre del cliente
nombreCliente = input("Ingrese nombre del cliente : ")
while not nombreCliente.isalpha() : 

    nombreCliente = input("Error , Ingrese nombre del cliente : ")

#validamos la cantidad de productos que va a ingresar el usuario 
cantidadProductos = input("Ingrese cantidad de productos : ")
while not cantidadProductos.isdigit() :

    cantidadProductos = input("ERROR , Ingrese cantidad de productos : ")

cantidadProductos = int(cantidadProductos)

for i in range(cantidadProductos) : 

#pedimos y validamos el ingreso del precio
    precioIngresado = input(f"Ingrese precio del producto {i+1} : ")
    while not precioIngresado.isdigit(): 

        precioIngresado = input(f"ERROR, Ingrese precio del producto {i+1} : ")
    
    precioIngresado = int(precioIngresado)

#preguntamos si el producto va a tener descuento
    tieneDescuento = input(f"El Producto {i+1} tiene descuento (n/s) : ").lower() 
    while tieneDescuento != "s" and tieneDescuento != "n" : 
        print("ERROR, Tiene que ingresar (S o N)...")
        tieneDescuento = input(f"ERROR , El Producto {i+1} tiene descuento (n/s) : ").lower() 

    acumuladorPrecio_SinDescuento += precioIngresado
    informacion += f"Producto {i+1} - Precio : {precioIngresado} Descuento (S/N) : {tieneDescuento} \n"

    if tieneDescuento == "s" :
    #aplicamos el descuento del 10%       
        precioFinal = precioIngresado * 0.9 
    else : 
        precioFinal = precioIngresado
        
    acumuladorPrecio_ConDescuento += precioFinal

ahorro = acumuladorPrecio_SinDescuento - acumuladorPrecio_ConDescuento
promedio = acumuladorPrecio_ConDescuento / cantidadProductos
#Mostramos la informacion por pantalla
print(f"\n\nCliente : {nombreCliente}" )
print(f"Cantidad de productos : {cantidadProductos}")
print(informacion)
print(f"Total Sin descuento : ${acumuladorPrecio_SinDescuento}")
print(f"Total Con descuento : ${acumuladorPrecio_ConDescuento}")
print(f"Ahorro : ${ahorro}")
print(f"Promedio por Producto : ${promedio}")
print("##################################### FIN #####################################\n\n")
