"""Definimos las variables que se van a utilizar en el programa:
    Tamaño de tablero, simbolos de agua, tiro, y blanco, los barcos con su longitud y nombre 
    y los mensajes que se van a repetir durante todo el juego.
"""
# Variables del juego
TAMANIO_TABLERO = 10
SIMBOLO_VACIO = '_'
SIMBOLO_TOCADO = 'X'
SIMBOLO_AGUA = 'O'
SIMBOLO_BARCO = 'B'

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