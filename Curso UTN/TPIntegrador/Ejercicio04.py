# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

# Nombre del agente
nombre = input("Ingrese nombre del agente: ")
while not nombre.isalpha() or nombre == "":
    print("Error, solo letras.")
    nombre = input("Ingrese nombre del agente: ")

print("\n--- INICIO DEL JUEGO ---")

# Bucle principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print(" La alarma bloqueó el sistema... DERROTA.")
        break

    print("\n----------------------------------------")
    print(f"Energía: {energia} | Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ACTIVA' if alarma else 'INACTIVA'}")
    print("----------------------------------------")

    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción inválida.")
        opcion = input("Opción: ")
        while not opcion.isdigit():
            print("Error: ingrese un número.")
            opcion = input("Opción: ")
        opcion = int(opcion)

    # OPCIÓN 1: FORZAR
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        # Anti-spam
        if forzar_seguidas == 3:
            alarma = True
            print("Forzaste demasiado... la cerradura se trabó y activaste la alarma.")
        
        else:
            # Riesgo si energía baja
            if energia < 40:
                riesgo = input("Energía baja. Elegí número 1-3: ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error.")
                    riesgo = input("Elegí número 1-3: ")
                if int(riesgo) == 3:
                    alarma = True
                    print(" Fallaste y activaste la alarma.")
                else:
                    if not alarma:
                        cerraduras_abiertas += 1
                        print(" Abriste una cerradura.")
            else:
                if not alarma:
                    cerraduras_abiertas += 1
                    print(" Abriste una cerradura.")

    # OPCIÓN 2: HACKEAR
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(" Hackeo completo. Se abrió una cerradura.")

    # OPCIÓN 3: DESCANSAR
    elif opcion == 3:
        tiempo -= 1
        forzar_seguidas = 0

        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print(" La alarma te desgasta (-10 energía extra).")

        print("Descansaste.")

print("\n--- RESULTADO ---")

if cerraduras_abiertas == 3:
    print(" VICTORIA. Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print(" DERROTA. Te quedaste sin recursos.")