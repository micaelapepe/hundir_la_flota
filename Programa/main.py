#import clases
import funciones
import variables as v


class tablero_placeholder:
    def __init__(self):
        pass


def inicializar_tableros():
    A = tablero_placeholder()
    B = tablero_placeholder()
    return A, B

def renderizar_tablero(tablero, esconder_bardos = True):
    pass




def turno_jugador(tablero_maquina):
    a, b = funciones.pedir_coordenadas()
    #tablero_maquina.impactar(a, b)
    pass

def turno_maquina(tablero_jugador):
    a, b = funciones.disparo_maquina(tablero_jugador)
    #tablero_jugador.impactar(a, b)
    pass


fin_juego_test = 3
def comprobar_fin_juego():
    global fin_juego_test
    fin_juego_test -= 1
    print(fin_juego_test)
    return fin_juego_test <= 0
        

def main():

    print("Empieza")
    t_jugador, t_maquina = inicializar_tableros()

    juego_terminado = False
    while not juego_terminado:
        turno_jugador(t_jugador)
        turno_maquina(t_maquina)
        renderizar_tablero(t_jugador, False)
        renderizar_tablero(t_maquina, True)
        juego_terminado = comprobar_fin_juego()

    print("Salida")

main()


