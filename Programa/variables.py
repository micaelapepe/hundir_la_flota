"""Definimos las variables que se van a utilizar en el programa:
    Tamaño de tablero, simbolos de agua, tiro, y blanco, los barcos con su longitud y nombre 
    y los mensajes que se van a repetir durante todo el juego.
"""
# Variables del juego
TAMANIO_TABLERO = 10
SIMBOLO_VACIO = '_'
SIMBOLO_TOCADO = 'X'
SIMBOLO_AGUA = 'O'

BARCOS = {
    'Portaaviones': 4,
    'Acorazado_1': 3,
    'Acorazado_2': 3,
    'Destructor_1': 2,
    'Destructor_2': 2,
    'Destructor_3': 2,
    'Submarino_1': 1,
    'Submarino_2': 1,
    'Submarino_3': 1,
    'Submarino_4': 1
    }
# Mensajes que se van a repetir durante todo el juego
MENSAJES = {
    'bienvenida': 'Bienvenido al juego de Hundir la Flota',
    'instrucciones': 'El objetivo del juego es hundir todos los barcos del oponente.',
    'turno_jugador': 'Es tu turno. Ingresa las coordenadas para disparara (ejemplo: A,1): ',
    'turno_computadora': 'Turno de la computadora.',
    'disparo_tocado': '¡Tocado!',
    'disparo_hundido': '¡Hundido!',
    'disparo_agua': '¡Agua!',
    'error_coordenadas': 'Coordenadas inválidas. Intenta de nuevo.',
    'error_repetido': 'Ya disparaste en esas coordenadas. Intenta de nuevo.',
    'ganador_jugador': '¡Felicidades! Has ganado.',
    'ganador_computadora': 'La computadora ha ganado. Mejor suerte la próxima vez.',
    'despedida': 'Gracias por jugar. ¡Hasta la próxima!'}

#Tablero alfanumerico para mostrar al jugador
# Crear un tablero vacío de 10x10 (letras A-J, números 1-10)
#Le preguntamos a la IA - GEMINI

# 1. Definir letras y números
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros = range(1, 11)

# 2. Crear el diccionario (¡en líneas separadas!)
tablero = {}
for letra in letras:
    for numero in numeros:
        tablero[(letra, numero)] = "~"  # '~' representa agua

# 3. ¡Pintar el tablero en pantalla!
# Primero, imprimimos la cabecera con las letras
print("      " + "   ".join(letras))
print("    " + "----" * len(letras) + "-")

# Luego, recorremos número por número para pintar cada fila
for numero in numeros:
    # Creamos el texto de la fila empezando por el número
    fila_str = f"{numero:2d} |"
    for letra in letras:
        # Añadimos lo que hay en el diccionario para esa coordenada
        fila_str += f"  {tablero[(letra, numero)]} "
    print(fila_str)