import variables as var

def pedir_coordenadas():

    while True:
        texto_in = input("Introduzca dos coordenadas de disparo (por ejemplo: 1, 5): ")
        division = texto_in.replace(",", " ").split()

        try:
            if len(division) != 2:
                raise ValueError("Formato incorrecto. Introduzca dos coordenadas separadas por espacios o comas")

            A = int(division[0])
            B = int(division[1])

            if not (0 <= A < var.TAMANIO_TABLERO and 0 <= B < var.TAMANIO_TABLERO):
                raise ValueError(f"Valores incorrectos. Las coordenadas deben estar entre 0 y {var.TAMANIO_TABLERO - 1}")

            return A, B
        
        except ValueError as error:
            print(error)

    
def disparo_maquina(tablero_rival):
    return 0, 0
    """Elige al azar una casilla a la que aún no se ha disparado (nunca repite)."""
    #libres = tablero_rival.casillas_sin_disparar()
    #fila, columna = libres[tablero_rival.rng.integers(len(libres))]
    #return int(fila), int(columna)

