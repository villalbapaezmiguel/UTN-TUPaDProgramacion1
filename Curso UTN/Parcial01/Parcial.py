opcion = ""
bandera = True
listas_herramientas = []
listas_existencias = []
cantidad_herramientas = -1
nombre_herramienta = ""
cantidad_existencia = -1

existe_herramienta = True
nombre_valido = False

while bandera == True :
#Menu del programa
    print("#################################- MENU -#################################\n")
    print("1)Carga Inicial de Herramientas")
    print("2)Carga de Existencias")
    print("3)Visualización de Inventario")
    print("4)Consulta de Stock (existencias)")
    print("5)Reporte de Agotados")
    print("6)Alta de Nuevo Producto")
    print("7)Actualización de Stock (Venta/Ingreso)")
    print("8)Salir del programa")

    opcion = input("Ingrese opcion (entre 1 y 8) : ")
#validamos que sea un numero
    while not opcion.isdigit() or opcion == "":
        print("Error , tiene que ser un numero...")
        opcion = input("Ingrese opcion (entre 1 y 8) : ")
    
    opcion = int(opcion)
#validamos que este dentro del rango de las opciones
    while (opcion > 8 or opcion <1) or opcion == "":
        print("Error , opcion invalida...")
        opcion = input("Ingrese opcion (entre 1 y 8) : ")
    opcion = int(opcion)

#estructura selectiva del menu
    if opcion == 1 :
        print("\n******************************* Carga Inicial de Herramientas *******************************")

#pedimos la cantidad de nombres de herramientas a agregar
        cantidad_herramientas = input("Ingrese la cantida de herramientas : ")
        while not cantidad_herramientas.isdigit() and int(cantidad_herramientas) > 0:
            print("Error, no es un numero...")
            cantidad_herramientas = input("Ingrese la cantidad de herramientas : ")
        cantidad_herramientas = int(cantidad_herramientas)

        for i in range(cantidad_herramientas) :
            nombre_herramienta = input("Ingrese nombre de la herramienta : ")

            while nombre_herramienta == "" or nombre_herramienta in listas_herramientas :
                
                print("Error, esa herramienta ya existe...")
                nombre_herramienta = input("Ingrese nuevamente el nombre de la herramienta : ")

            listas_herramientas.append(nombre_herramienta)

#prueba para ver los resultados
        print(listas_herramientas)

    elif opcion == 2 :
        print("\n******************************* Carga de Existencias *******************************")
        indice = 0
        for elemento in range(len(listas_herramientas)) :

            print(f"Herramienta : {listas_herramientas[indice]}")
            stock_herramienta = input("Ingrese stock : ")
#Validamos que nos haya ingresado bien el stock
            while not stock_herramienta.isdigit() and int(stock_herramienta) > 0:
                print("Error, no es un numero...")
                stock_herramienta = input("Ingrese la cantidad de herramientas : ")
            stock_herramienta = int(stock_herramienta)

            listas_existencias.append(stock_herramienta)
            indice += 1
    elif opcion == 3 :
        print("\n******************************* Visualización de Inventario *******************************")
        
        for herramienta , cantidad in zip(listas_herramientas, listas_existencias) : 
            print(f"Herramienta : {herramienta} | Cantidad : {cantidad}")



    elif opcion == 4 :
        print("\n******************************* Consulta de Stock (existencias) *******************************")
        bandera_stock = False
        nombre = input("Ingrese nombre de la herramienta : ")

        for herramienta , cantidad in zip(listas_herramientas,listas_existencias) :

            if nombre == herramienta :
                print(f"Unidades encontradas : {cantidad}")
                bandera_stock = True

        if bandera_stock == False :
            print("Error, No se encontro la herramienta...")

    elif opcion == 5 :
        print("\n******************************* Reporte de Agotados *******************************")
        
        for herramienta , cantidad in zip(listas_herramientas, listas_existencias) : 
            if cantidad == 0 :
                print(f"Herramienta : {herramienta} | cantidad : {cantidad}")

    elif opcion == 6 :
        print("\n******************************* Alta de Nuevo Producto *******************************")
        nueva_herramienta = input("Ingrese nueva herramienta : ")

        while nueva_herramienta == "" or nueva_herramienta in listas_herramientas :
                
                print("Error, esa herramienta ya existe...")
                nombre_herramienta = input("Ingrese nuevamente el nombre de la herramienta : ")

        listas_herramientas.append(nueva_herramienta)

        cantidad = input("Ingrese cantidad de stock")
        while not stock_herramienta.isdigit() and int(stock_herramienta) > 0:
            print("Error, no es un numero...")
            stock_herramienta = input("Ingrese la cantidad de herramientas : ")
        stock_herramienta = int(stock_herramienta)

        listas_existencias.append(cantidad)

    elif opcion == 7 :
        print("\n******************************* Actualización de Stock (Venta/Ingreso) *******************************")
        
    
    
    elif opcion == 8 :
        bandera = False
        print("Fin del programa...")













