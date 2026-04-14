#La arena del gladiador 

#variables 
nombreDel_jugador = ""
jugador_hp = 100
enemigo_hp = 100
turno_jugador = True
opcion = -1
pociones = 3

#configuracion del personaje :

print("------------------- BIENVENIDO A LA ARENA -------------------")
nombreDel_jugador = input("Nombre del Gladiador : ")

while not nombreDel_jugador.isalpha():

    print("Error: Solo se permiten letras")
    nombreDel_jugador = nombreDel_jugador = input("Nombre del Gladiador : ")

#inicializacion de estadisticas 
print("==================== INICIO DEL COMBATE ====================")

while jugador_hp > 0 and enemigo_hp > 0 :

    print(f"{nombreDel_jugador} (HP : {jugador_hp}) vs Enemigo (HP : {enemigo_hp} | Pociones : {pociones})")
#Mostramos el menu
    print("Elige accion :")
    print("1. Ataque Pesado \n2. Rafaga Veloz\n3. Curar")

#Validamos la opcion
    opcion = input("Opcion : ")

    while not opcion.isdigit():
        print("Error: ingrese un número valido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: ingrese un número valido.")
        opcion = input("Opción: ")
        while not opcion.isdigit():
            print("Error: ingrese un número valido.")
            opcion = input("Opción: ")
        opcion = int(opcion)

    if opcion == 1 :
        print(">> ¡Inicia Ataque Pesado !")

        if enemigo_hp < 20 :

            print("Golpe Critico !!!")
            enemigo_hp -= 15 * 1.5
            jugador_hp -12
            print(f"¡Atacaste al enemigo por {15 * 1.5} puntos de daño!")
            print("¡El enemigo te ataco por 12 puntos de daño !")
        else : 
            enemigo_hp -= 15
            jugador_hp -= 12
            print("¡Atacaste al enemigo por 15 puntos de daño!")
            print("¡El enemigo te ataco por 12 puntos de daño !")

    elif opcion == 2 :
        print(">> ¡Inicia Rafaga de Golpes !")

        for i  in range(3):
            i += 1

            enemigo_hp -= 5
            print(">> Golpe Conectado por 5 de daño ")

        print("¡El enemigo te ataco por 12 puntos de daño !")
    elif opcion == 3 : 
        print(">> ¡Inicia Curacion !")

        if pociones > 0 :
            jugador_hp += 30
            pociones -= 1
            jugador_hp -= 12
            print("¡El enemigo te ataco por 12 puntos de daño !")
        else :

            print("¡No te quedan pociones!")
            jugador_hp -= 12
            print("¡El enemigo te ataco por 12 puntos de daño !")

    else : 
        print("Error: ingrese un número valido.")

    
if jugador_hp > 0 : 
    print(f"¡VICTORIA! {nombreDel_jugador} ha ganado la batalla.")
elif jugador_hp <= 0 :
    print(f"¡DERROTA!. Has caido en combate.")









