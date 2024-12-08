
import random  # Importamos la biblioteca que nos permite generar elecciones aleatorias.

# Definimos una lista en la variable "opciones" que el jugador podrá escoger.
# Cada item entre comillas representa una opción.
opciones = ["Piedra", "Papel", "Tijera"]  

# Se define la función "evaluar_resultado" con las variables "jugador" y "computadora" donde vamos a realizar los,
# condicionales con los operadores lógicos que nos permitirán procesar los resultados,
# Indicándonos si el jugador gana, pierde o empata, devolviendonos un mensaje con el resultado del juego,
# que nos servirá posteriormente para comparar resultados y presesntarlos. 
def evaluar_resultado(jugador, computadora): 

    if jugador == computadora: # Se establece condicional if con el operador racional de igualdad "==".
        return "Empate"  #En caso de cumplirse la igualdad del condicional determina empate.
        #Para elif se establecen condiciones mediante el operador lógico "and" Y "or" que se deben cumplir para que el jugador gane, tomando 
        #los elementos de piedra papel o tijera de acuerdo a su posición en la lista iniciando por "0" que sería Piedra, "1" que sería
        #Papel y "2" que sería tijera.
    elif (jugador == 0 and computadora == 2) or \
         (jugador == 1 and computadora == 0) or \
         (jugador == 2 and computadora == 1):  
        return "Ganaste" #En caso que no se cumpla el if y se cumpla una de estas condiciones nos devuelve que ganamos.
    else:
        return "Perdiste" #Sino se cumplen ni el if ni los elif nos devuelve que perdimos.

# Iniciamos un bucle while true que nos permitirá mantenernos dentro del juego hasta seleccionar la opción para salir.
while True:
    
    print("\n JUEGO DE PIEDRA, PAPEL O TIJERA ") #Mostramos al jugador el nombre del juego
    print("\nElige una opción:") #Desplegamos el menú del juego con sus opciones.
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir del juego")

    # Utilizamos el bloque try para manejar los errores que podrían suceder.
    try:
        jugador_eleccion = int(input("\nIngresa tu elección del (1-4): ")) #Declaramos una variable entera para que el jugador ingrese una opción.
    except ValueError:  # En caso que no ingrese un valor válido nos indicará.
        print("⚠️ Por favor, ingresa un número válido (1-4).")
        continue # Una vez que nos indica "continue" hará que el se reinicie el bucle.

    # Verificamos si el jugador eligió salir.
    if jugador_eleccion == 4: #Verificamos si el jugador ingresó la opción la 4.
        print("👋 ¡Gracias por jugar! Hasta luego.")
        break #Se utiliza la función break para salir anticipadamente del bucle.

    # Validamos si la elección es válida (1, 2, o 3).
    if not (1 <= jugador_eleccion <= 3):  # Uso de operador lógico para validar rango.
        print("⚠️ Opción no válida. Intenta de nuevo.")
        continue #Volvemos a iniciar el bucle

    # Como en una lista la primera posición es cero hay que restar 1 para que no se vea afectada la elección del jugador
    jugador_eleccion -= 1

    # La computadora elige aleatoriamente.
    computadora_eleccion = random.randint(0, 2) #Se crea la variable random en la cual se almacena una opción aleatoria de la lista que puede
    #Ser 0=Piedra, 1=Papel, 2=Tijera.

    # Mostramos las elecciones del jugador y de la computadora
    print(f"\nTu elección: {opciones[jugador_eleccion]}") #Usamos f/strings para concatenar el print.
    print(f"\nElección de la computadora: {opciones[computadora_eleccion]}")

    # Llamamos a la funcion evualuar_resultado con los argumentos de la elección del jugador y la respuesta aleatoria de la computadora
    # Y lo guardamos en la variable resultado 
    resultado = evaluar_resultado(jugador_eleccion, computadora_eleccion)

    # Evaluamos con condicionales la variable resultado y la comparamos para imprimir los mensajes.
    if resultado == "Empate":
        print("🤝 Resultado: ¡Es un empate!")
    elif resultado == "Ganaste":
        print("🎉 Resultado: ¡Haz Ganado!")
    else:
        print("😞 Resultado: Perdiste")

    # Explicamos el resultado para quienes no tienen claras las reglas del juego a través de condicionales y operadores racionales.
    if jugador_eleccion == 0 and computadora_eleccion == 2:
        print("✔️ La Piedra rompe a la Tijera")
    elif jugador_eleccion == 1 and computadora_eleccion == 0:
        print("✔️ El Papel cubre a la Piedra")
    elif jugador_eleccion == 2 and computadora_eleccion == 1:
        print("✔️ la Tijera corta el Papel")
    elif computadora_eleccion == 0 and jugador_eleccion == 2:
        print("❌ La Piedra rompe a la Tijera")
    elif computadora_eleccion == 1 and jugador_eleccion == 0:
        print("❌ El Papel cubre a la Piedra")
    elif computadora_eleccion == 2 and jugador_eleccion == 1:
        print("❌ La Tijera corta el Papel")
