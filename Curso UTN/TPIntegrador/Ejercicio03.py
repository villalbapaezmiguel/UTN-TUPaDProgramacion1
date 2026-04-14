#agenda de turnos con nombres sin listas 
nombreOperador = ""
opcion = -1
bandera = True
dia = 0
nombrePaciente = ""

#Turnos Lunes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

#Turnos Martes
martes1 = ""
martes2 = ""
martes3 = ""

# Contadores
contadorOcupado_lunes = 0
contadorOcupado_martes = 0


nombreOperador = input("Ingrese nombre del operador : ")#despues validar como minimo 4 caractres
while not nombreOperador.isalpha() or nombreOperador == "":
    print("Error , solo letras ")
    nombreOperador = input("Ingrese nombre del operador : ")

while bandera == True : 
    print("1. Reservar turno ")
    print("2. Cancelar turno ")
    print("3. Ver agenda del dia ")
    print("4. Ver resumen general ")
    print("5. Cerrar sistema ")

    opcion = input("Opcion (Entre 1 y 5): ")
    while not opcion.isdigit() : 
        print("Error , Opcion ivalida...")
        opcion = input("Opcion (Entre 1 y 5): ")

    opcion = int(opcion)
    while opcion < 1 or opcion > 5 : 
        print("Error , tiene que ser entre 1 y 5")
        opcion = input("Opcion (entre 1 y 5): ")

        while not opcion.isdigit() : 
            print("Error , Opcion ivalida...")
            opcion = input("Opcion (Entre 1 y 5): ")
        opcion = int(opcion)

    if opcion == 1 :
        print("\n#########################-RESERVAR TURNO-#########################")
        print("Dias disponibles : \n 1. Lunes \n 2. Martes")
#Validamos que lo que haya ingresado sea un numero y sea 1 o 2
        dia = input("Seleccione dia : ")
        while not dia.isdigit() : 
            print("Error, Dias disponibles : \n 1. Lunes \n 2. Martes")
            dia = input("Seleccione dia : ")

        dia = int(dia)
        while dia < 1 or dia > 2 : 
            print("Error, Dias disponibles : \n 1. Lunes \n 2. Martes")
            dia = input("Seleccione dia : ")

            while not dia.isdigit() : 
                print("Error, Dias disponibles : \n 1. Lunes \n 2. Martes")
                dia = input("Seleccione dia : ")

            dia = int(dia)
            
#pedimos el nombre del paciente
        nombrePaciente = input("Ingrese nombre del paciente : ")
        while not nombrePaciente.isalpha():
            print("Error , solo letras...")
            nombrePaciente = input("Ingrese nombre del paciente : ").lower()

        if dia == 1 :

            if nombrePaciente == lunes1 or nombrePaciente == lunes2 or nombrePaciente == lunes3 or nombrePaciente == lunes4 :
                print("Ese paciente ya tiene un turno resrvado...")
            else :
                if lunes1 == "":
                    lunes1 = nombrePaciente 
                    print("Se guardo exitosamente en el primer lunes!!")
                
                elif lunes2 == "":
                    lunes2 = nombrePaciente
                    print("Se guardo exitosamente en el segundo lunes!!")
                
                elif lunes3 == "" :
                    lunes3 = nombrePaciente 
                    print("Se guardo exitosamente en el tercer lunes!!")                
                elif lunes4 == "":
                    lunes4 = nombrePaciente
                    print("Se guardo exitosamente en el cuarto lunes!!")
                else : 
                    print("No hay mas lugar...")
        elif dia == 2 :

            if nombrePaciente == martes1 or nombrePaciente == martes2 or nombrePaciente == martes3:
                print("Ese paciente ya tiene un turno resrvado...")
            else :

                if martes1 == "":
                    martes1 = nombrePaciente 
                    print("Se guardo exitosamente en el primer Martes!!")
                elif martes2 == "" :
                    martes2 = nombrePaciente 
                    print("Se guardo exitosamente en el Segundo Martes!!")
                elif martes3 == "":
                    martes3 = nombrePaciente 
                    print("Se guardo exitosamente en el tercer Martes!!")
                else : 
                    print("No hay mas lugar...")                                        

        print("#########################################################################\n")
    elif opcion == 2 :
        print("\n#########################-CANCELAR TURNO-#########################")
        dia = input("Seleccione dia : ")
        while not dia.isdigit() : 
            print("Error, Dias disponibles : \n 1. Lunes \n 2. Martes")
            dia = input("Seleccione dia : ")

        dia = int(dia)
        while dia < 1 or dia > 2 : 
            print("Error, Dias disponibles : \n 1. Lunes \n 2. Martes")
            dia = input("Seleccione dia : ")

            while not dia.isdigit() : 
                print("Error, Dias disponibles : \n 1. Lunes \n 2. Martes")
                dia = input("Seleccione dia : ")

            dia = int(dia)
            
#pedimos el nombre del paciente
        nombrePaciente = input("Ingrese nombre del paciente : ")
        while not nombrePaciente.isalpha() or nombrePaciente == "":
            print("Error , solo letras...")
            nombrePaciente = input("Ingrese nombre del paciente : ").lower()

#Si existe, cancelar y dejar el espacio vacío ("")

        if dia == 1 :

            if nombrePaciente == lunes1 :
                lunes1 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            elif nombrePaciente == lunes2 :
                lunes2 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            elif nombrePaciente == lunes3 :
                lunes3 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            elif nombrePaciente == lunes4 :
                lunes4 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            else : 
                print("Error, NO existe ese paciente...")
        
        elif dia == 2:
            if nombrePaciente == martes1 :
                martes1 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            elif nombrePaciente == martes2 :
                martes2 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            elif nombrePaciente == martes3 :
                martes3 = ""
                print (f"Se cancelo el turno de {nombrePaciente}...")
            else :
                print("Error, NO existe ese paciente...")
    
        print("#########################################################################\n")
    elif opcion == 3 : 
        print("\n#########################-VER AGENDA DEL DIA-#########################")
        print("Turnos Lunes :")
        if lunes1 == "":
            print(f"Primer lunes : libre..")
        else : 
            print(f"Primer lunes : ocupado ")

        if lunes2 == "":
            print(f"Segundo lunes : libre..")
        else : 
            print(f"Segundo lunes : ocupado ")

        if lunes3 == "":
            print(f"Tercer lunes : libre..")
        else : 
            print(f"Tercer lunes : ocupado ")

        if lunes4 == "":
            print(f"Cuarto lunes : libre..")
        else : 
            print(f"Cuarto lunes : ocupado ")

        print("Turnos Martes :")

        if martes1 == "":
            print(f"Primer martes : libre..")
        else : 
            print(f"Primer martes : ocupado ")

        if martes2 == "":
            print(f"Segundo martes : libre..")
        else : 
            print(f"Segundo martes : ocupado ")

        if martes3 == "":
            print(f"Tercer martes : libre..")
        else : 
            print(f"Tercer martes : ocupado ")
        print("#########################################################################\n")
    elif opcion == 4: 
        print("\n#########################-RESUMEN GENERAL-#########################")

# Contar lunes
        if lunes1 != "":
            contadorOcupado_lunes += 1
        if lunes2 != "":
            contadorOcupado_lunes += 1
        if lunes3 != "":
            contadorOcupado_lunes += 1
        if lunes4 != "":
            contadorOcupado_lunes += 1

# Contar martes
        if martes1 != "":
            contadorOcupado_martes += 1
        if martes2 != "":
            contadorOcupado_martes += 1
        if martes3 != "":
            contadorOcupado_martes += 1

# Libres
        libres_lunes = 4 - contadorOcupado_lunes
        libres_martes = 3 - contadorOcupado_martes

# Mostrar resumen
        print(f"Lunes -> Ocupados: {contadorOcupado_lunes} | Libres: {libres_lunes}")
        print(f"Martes -> Ocupados: {contadorOcupado_martes} | Libres: {libres_martes}")

# Comparación
        if contadorOcupado_lunes > contadorOcupado_martes:
            print("Día con más turnos: Lunes")
        elif contadorOcupado_martes > contadorOcupado_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate en cantidad de turnos")

        print("#########################################################################\n")
    elif opcion == 5 :
        print("Fin del programa...")
        bandera = False
