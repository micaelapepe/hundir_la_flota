"""Programa principal de Hundir la Flota: jugador contra máquina por turnos."""

import funciones
import variables as v


def inicializar_tableros():
    """Crea los tableros del jugador y de la máquina con sus barcos.

    Returns:
        tuple[Tablero, Tablero]: (tablero del jugador, tablero de la máquina).
    """
    A = funciones.preparar_tablero()
    B = funciones.preparar_tablero()
    return A, B


def renderizar_tablero(tablero, esconder_barcos=True):
    """Imprime un tablero.

    Args:
        tablero (Tablero): tablero que se imprime.
        esconder_barcos (bool): True para ocultar los barcos (tablero rival).
    """
    print(tablero.mostrar(mostrar_barcos=not esconder_barcos))
    print()


def turno_jugador(tablero_maquina):
    """Turno del jugador: dispara hasta que falla o hunde todos los barcos.

    Si repite una casilla, vuelve a pedir coordenadas.

    Args:
        tablero_maquina (Tablero): tablero de la máquina.
    """
    while True:
        coordenada = funciones.pedir_coordenadas()
        resultado = tablero_maquina.recibir_disparo(coordenada)
        print(v.MENSAJES[resultado])

        if resultado == 'error_repetido':
            continue
        if resultado == 'disparo_agua' or tablero_maquina.todos_hundidos():
            return
        renderizar_tablero(tablero_maquina, True)  # tocado: vuelve a disparar


def turno_maquina(tablero_jugador):
    """Turno de la máquina: dispara al azar hasta que falla o hunde todos los barcos.

    Args:
        tablero_jugador (Tablero): tablero del jugador.
    """
    print(v.MENSAJES['turno_computadora'])
    while True:
        coordenada = funciones.disparo_maquina(tablero_jugador)
        resultado = tablero_jugador.recibir_disparo(coordenada)
        fila, columna = coordenada
        letra = chr(ord('A') + columna)
        print(f"La máquina dispara a {letra}, {fila + 1}: {v.MENSAJES[resultado]}")
        if resultado == 'disparo_agua' or tablero_jugador.todos_hundidos():
            return


def comprobar_fin_juego(tablero_jugador, tablero_maquina):
    """Comprueba si alguien ha ganado e imprime el mensaje del ganador.

    Args:
        tablero_jugador (Tablero): tablero del jugador.
        tablero_maquina (Tablero): tablero de la máquina.

    Returns:
        bool: True si la partida ha terminado.
    """
    if tablero_maquina.todos_hundidos():
        print(v.MENSAJES['ganador_jugador'])
        return True
    if tablero_jugador.todos_hundidos():
        print(v.MENSAJES['ganador_computadora'])
        return True
    return False


def main():
    """Ejecuta la partida: muestra los tableros y alterna turnos hasta que alguien gana."""
    funciones.mostrar_bienvenida()
    t_jugador, t_maquina = inicializar_tableros()

    while True:
        print("=== TU TABLERO ===")
        renderizar_tablero(t_jugador, False)
        print("=== TABLERO DE LA MÁQUINA ===")
        renderizar_tablero(t_maquina, True)

        turno_jugador(t_maquina)
        if comprobar_fin_juego(t_jugador, t_maquina):
            break

        turno_maquina(t_jugador)
        if comprobar_fin_juego(t_jugador, t_maquina):
            break

    print(v.MENSAJES['despedida'])



main()
