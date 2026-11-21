"""Funciones auxiliares del juego: preparar tableros, leer coordenadas y disparo de la máquina."""

import numpy as np

import variables as var
from Clases import Barcos, Tablero


def mostrar_bienvenida():
    """Imprime el mensaje de bienvenida y las instrucciones."""
    print(var.MENSAJES['bienvenida'])
    print(var.MENSAJES['instrucciones'])
    print()


def preparar_tablero():
    """Crea un tablero con todos los barcos de BARCOS colocados al azar.

    Coloca primero los barcos más largos. Si alguno no cabe, empieza de nuevo
    con un tablero vacío.

    Returns:
        Tablero: tablero con todos los barcos colocados.
    """
    while True:
        tablero = Tablero()
        # Primero los más largos: es más fácil que quepan todos
        longitudes = sorted(var.BARCOS.values(), reverse=True)
        if all(tablero.colocar_barco_aleatorio(Barcos(longitud)) for longitud in longitudes):
            return tablero


def pedir_coordenadas():
    """Pide al jugador una coordenada (por ejemplo, «A, 5») hasta que sea válida.

    Returns:
        tuple[int, int]: (fila, columna) empezando en 0.
    """
    while True:
        texto_in = input("Introduzca las coordenadas de disparo (por ejemplo: A, 5): ")
        division = texto_in.replace(",", " ").split()

        try:
            if len(division) != 2 or len(division[0]) != 1:
                raise ValueError("Formato incorrecto. Introduzca una letra y un número separados por espacios o comas")

            A = int(division[1]) - 1                     # fila: el número (1 a 10)
            B = ord(division[0].upper()) - ord('A')      # columna: la letra (A a J)

            if not (0 <= A < var.TAMANIO_TABLERO and 0 <= B < var.TAMANIO_TABLERO):
                ultima_letra = chr(ord('A') + var.TAMANIO_TABLERO - 1)
                raise ValueError(f"Valores incorrectos. La letra debe estar entre A y {ultima_letra} y el número entre 1 y {var.TAMANIO_TABLERO}")

            return A, B

        except ValueError as error:
            print(error)


def disparo_maquina(tablero_rival):
    casillas = tablero_rival.casillas

    sin_disparar = ~np.isin(casillas, [var.SIMBOLO_TOCADO, var.SIMBOLO_AGUA])
    libres = np.argwhere(sin_disparar)
    fila, columna = libres[np.random.randint(len(libres))]
    return int(fila), int(columna)
