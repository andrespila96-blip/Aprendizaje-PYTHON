menos = 1
mas = 100
intentos = 0
jugando = True


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
    if respuesta == "si" or respuesta == "no":
        break
    else:
        print("\nDISCULPAME NO TE ENTIENDO. SOLO DIME 'si' o 'no'.")

if respuesta == "si":
    print("\n¡GENIAL NO TE ARREPENTIRAS! ")

elif respuesta == "no":
    print("\n¡YA ESTAS DE ABURRIDO! VAMOS TE VAS A DIVERTIR TE LO JURO: ")

print("\nQUIERO QUE PIENSES UN NUMERO DEL 1 AL 100 PERO NO ME LO DIGAS")

print("\nVOY ADIVINAR EL NUMERO QUE ESTAS PENSADO ¡NO HAGAS TRAMPA ASI QUE ANOTA EL NUMERO!\n")

while jugando:
        intentos += 1
        intento_maquina = (menos + mas) // 2
        
        print("¿Tu número es el", intento_maquina, "?")
        pista = input("Tu respuesta: ").lower()
        print()       

        if pista == "correcto":
            print("¡TE GANE LO SABIA! Y SOLO ME TOMO", intentos, "INTENTOS")
            jugando = False
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