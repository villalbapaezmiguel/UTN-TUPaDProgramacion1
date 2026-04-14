#Acceso al Campus y Menú Seguro
#variables
nombreUsuario = ""
clave = ""
bandera = True
contadorIntentos = 0
informacion = ""
opcion = -1
claveNueva = ""
claveConfirmacion = ""


nombreUsuario = input("Ingrese nombre de Usuario : ").lower()
clave = input("Ingrese clave : ").lower()
while nombreUsuario != "alumno" or clave != "python123" : 
    contadorIntentos += 1
    print(f"Intentos {contadorIntentos}/3 - Usuario : {nombreUsuario} ")
    print(f"Clave : {clave}")
    print("ERROR , Credenciales invalidas \n")

    if contadorIntentos >= 3 :
        print("Cuenta bloqueada")
        bandera = False
        break

    nombreUsuario = input("Ingrese nombre de Usuario : ").lower()
    clave = input("Ingrese clave : ").lower()
    

while bandera == True :

    print("1)Ver estado de inscripcion ")
    print("2)Cambiar clave ")
    print("3)Mostrar mensaje motivacional")
    print("4)Salir")

    opcion = input("Opcion (entre 1 y 4): ")
#valida que lo que haya entrado sea un numero
    while not opcion.isdigit() : 
        print("Error : Opcion fuera de rango ")
        opcion = input("Opcion (entre 1 y 4): ")
    opcion = int(opcion)
#validamos que lo que la opcion elegida este entre 1 y 4 
    while opcion < 1 or opcion > 4 :
        print("Error : Opcion fuera de rango ")
        opcion = input("Opcion (entre 1 y 4): ")

        while not opcion.isdigit() : 
            print("Error : Opcion fuera de rango ")
            opcion = input("Opcion (entre 1 y 4): ")
            
        opcion = int(opcion)


    if opcion == 1 : 
        print("\n#########################-ESTADO DE INSCRIPCION-#########################")
        print("ESTADO : Inscripto\n")
        print("#########################################################################\n")
    elif opcion == 2 :
        print("\n#########################-CAMBIAR CLAVE-#########################")
#pedir nueva clave y confirmacion (deben coincidir )
        claveNueva = input("Ingrese nueva clave (minimo 6 caracteres): ")
        while len(claveNueva) < 6 :
            claveNueva = input("ERROR ,Ingrese nueva clave (minimo 6 caracteres): ")

#pedimos que escriba la clave nuevamente 
        claveConfirmacion = input("Ingrese nuevamente la clave (minimo 6 caracteres): ")
        while len(claveConfirmacion) < 6 :
            claveConfirmacion = input("ERROR ,Ingrese nuevamente la clave (minimo 6 caracteres): ")
#Varificamos que sean iguales 
        if claveNueva == claveConfirmacion : 
            print("Clave cambiada con exito !!!\n")
        else :
            print("Clave rechazada...\n")
        print("#########################################################################\n")
    elif opcion == 3 : 
        print("\n#########################-MENSAJE MOTIVACIONAL-#########################")
        print("Si te frustrás, vas por buen camino...")
        print("#########################################################################\n")
    elif opcion == 4 : 
        print("Fin del programa...")
        bandera = False












