menos = 1
mas = 100
intentos = 0
jugando = True
opciones_validas = ("si", "no")
historial_intentos = []

print()
print()
print("██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  ")
print("██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██ ")
print("██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██ ")
print("██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██ ")
print("██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████  \n")

print("\nIniciando en...")
for i in range(3, 0, -1):
        print(i)

while True:
    respuesta= input("\n¿QUIERES JUGAR UN JUEGO?: ").lower().strip()
    if respuesta in opciones_validas:
        break
    else:
        print(f"\nDISCULPAME NO TE ENTIENDO. SOLO DIME '{opciones_validas[0]}' o '{opciones_validas[1]}'.")

if respuesta == "no":
    print("\n¡YA ESTAS DE ABURRIDO! VAMOS TE VAS A DIVERTIR TE LO JURO")
    jugando = False
    print()
    print()

if respuesta == "si":
    print("\n¡GENIAL NO TE ARREPENTIRAS! ")
    print("\nQUIERO QUE PIENSES UN NUMERO DEL 1 AL 100 PERO NO ME LO DIGAS")
    print("\nVOY ADIVINAR EL NUMERO QUE ESTAS PENSADO ¡NO HAGAS TRAMPA ASI QUE ANOTA EL NUMERO! ")

while jugando:
        if menos > mas:
             print("¡Espera un segundo! Me estas haciendo trampa\n")
             print("¡ASI YO NO JUEGO CON USTED! ¡ADIOS!\n")
             jugando = False
             break
        
        intentos += 1
        intento_maquina = (menos + mas) // 2

        historial_intentos.append(intento_maquina)
        
        print("¿Tu número es el", intento_maquina, "?")
        pista = input("Tu respuesta: ").lower()
        print()       

        if pista == "correcto":
            print("¡TE GANE LO SABIA! Y SOLO ME TOMO", intentos, "INTENTOS\n")
            jugando = False

            print("📋 HISTORIAL DE MIS INTENTOS (RECORRIENDO LA LISTA):")
            for num in historial_intentos:
                 print(f" -> Intenté con el número: {num}")
            print()

            resumen_partida = {
                      "resultado": "Victoria de la Máquina",
                      "intentos_usados": intentos,
                      "rango_final_menos": menos,
                      "rango_final_mas": mas}
            print()
                 
            print("📊 ESTADÍSTICAS GUARDADAS EN EL DICCIONARIO:")
            print("Estado:", resumen_partida["resultado"])
            print("Total Intentos:", resumen_partida["intentos_usados"])
            print("-" * 40, "\n")
            print()

        elif pista == "mas":
            menos = intento_maquina + 1
            print()

        elif pista == "menos":
            mas = intento_maquina - 1
            print()

        else:
            print("Respuesta inválida. Intenta de nuevo")
            intentos -= 1
            historial_intentos.pop()
print()
print() 
print(" ██████  ██████   █████   ██████ ██  █████  ██████")
print("██       ██   ██ ██   ██ ██      ██ ██   ██ ██    ")
print("██   ███ ██████  ███████ ██      ██ ███████ ██████")
print("██    ██ ██   ██ ██   ██ ██      ██ ██   ██     ██")
print(" ██████  ██   ██ ██   ██  ██████ ██ ██   ██ ██████\n")

print("      ██████   ████  ██████       ██ ██  ██   ██████  █████  ██████")
print("      ██   ██ ██  ██ ██   ██      ██ ██  ██  ██      ██   ██ ██   ██")
print("      ██████  ██  ██ ██████   ██  ██ ██  ██  ██   ██ ███████ ██████ ")
print("      ██      ██  ██ ██   ██  ██  ██ ██  ██  ██   ██ ██   ██ ██   ██")
print("      ██       ████  ██   ██   ████  ██████   ██████ ██   ██ ██   ██\n")