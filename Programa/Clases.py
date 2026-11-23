"""Clases del juego: Barcos (cada barco y sus impactos) y Tablero (cuadrícula de NumPy)."""

import numpy as np

from variables import *

class Barcos:
	"""Un barco: sabe cuánto mide y cuántos impactos ha recibido."""
	def __init__(self, longitud):
		"""Crea un barco sin impactos.

		Args:
		    longitud (int): número de casillas que ocupa el barco.

		Raises:
		    ValueError: si la longitud es menor o igual que cero.
		"""
		if longitud <= 0:
			raise ValueError("La longitud debe ser mayor que cero") 
		self.longitud = longitud
		self.impactos = 0

	def recibir_impacto(self):
		"""Registra un impacto y devuelve si el barco ha sido hundido."""
		if self.impactos < self.longitud:
			self.impactos += 1
		return self.esta_hundido()

	def esta_hundido(self):
		"""Devuelve True si el barco ha recibido tantos impactos como su longitud."""
		return self.impactos >= self.longitud
    
#-- CLASE TABLERO

class Tablero:
    """Tablero de juego de un jugador.

    Atributos:
        tamanio (int): número de filas y de columnas.
        casillas (np.ndarray): cuadrícula con SIMBOLO_VACIO, SIMBOLO_BARCO,
            SIMBOLO_TOCADO o SIMBOLO_AGUA en cada casilla.
        barcos (list[Barcos]): barcos colocados en el tablero.
        ocupadas (dict): (fila, columna) -> barco que ocupa esa casilla.
    """
    def __init__(self, tamanio=TAMANIO_TABLERO):
        """Crea un tablero vacío, sin barcos.

        Args:
            tamanio (int): número de filas y de columnas. Por defecto, TAMANIO_TABLERO.
        """
        self.tamanio = tamanio
        self.casillas = np.full((tamanio, tamanio), SIMBOLO_VACIO)
        self.barcos = []
        self.ocupadas = {}        # (fila, columna) -> Barco

    # --- colocación -------------------------------------------------------
    def _en_limites(self, fila, columna):
        """Devuelve True si (fila, columna) está dentro del tablero."""
        return 0 <= fila < self.tamanio and 0 <= columna < self.tamanio

    def _hay_barco_cerca(self, fila, columna):
        """Comprueba si hay un barco en la casilla o en alguna de las 8 de alrededor.

        Recorta del array una zona de 3 x 3 (más pequeña en los bordes) y mira si
        alguna casilla es SIMBOLO_BARCO.

        Returns:
            bool: True si hay algún barco en esa zona.
        """
        r_min = max(0, fila - 1)
        r_max = min(self.tamanio, fila + 2)
        c_min = max(0, columna - 1)
        c_max = min(self.tamanio, columna + 2)
        trozo = self.casillas[r_min:r_max, c_min:c_max]
        return (trozo == SIMBOLO_BARCO).any()
    
        #for df in (-1, 0, 1):
        #    for dc in (-1, 0, 1):
        #        if (fila + df, columna + dc) in self.ocupadas:
        #            return True
        #return False

    def puede_colocar(self, posiciones):
        """Comprueba si un barco cabe en esas posiciones.

        Todas las casillas deben estar dentro del tablero y sin barcos alrededor.

        Args:
            posiciones (list[tuple[int, int]]): casillas (fila, columna) del barco.

        Returns:
            bool: True si se puede colocar.
        """
        return all(
            self._en_limites(f, c) and not self._hay_barco_cerca(f, c)
            for f, c in posiciones
        )

    def colocar_barco(self, barco, fila, columna, horizontal):
        """Coloca un barco a partir de una casilla, en horizontal o en vertical.

        Si cabe, marca sus casillas con SIMBOLO_BARCO en el array y las guarda en
        `ocupadas` y en `barco.posiciones`.

        Args:
            barco (Barcos): barco que se coloca.
            fila (int): fila de la primera casilla.
            columna (int): columna de la primera casilla.
            horizontal (bool): True hacia la derecha, False hacia abajo.

        Returns:
            bool: True si se ha colocado, False si no cabe.
        """
        posiciones = [
            (fila, columna + i) if horizontal else (fila + i, columna)
            for i in range(barco.longitud)
        ]
        if not self.puede_colocar(posiciones):
            return False
        barco.posiciones = posiciones
        for posicion in posiciones:
            self.ocupadas[posicion] = barco
            self.casillas[posicion] = SIMBOLO_BARCO
        self.barcos.append(barco)
        return True

    def colocar_barco_aleatorio(self, barco, intentos=1000):
        """Intenta colocar un barco en una posición y orientación al azar.

        Args:
            barco (Barcos): barco que se coloca.
            intentos (int): número máximo de posiciones que se prueban.

        Returns:
            bool: True si se ha colocado, False si no ha cabido en ningún intento.
        """
        for _ in range(intentos):
            fila = np.random.randint(self.tamanio)
            columna = np.random.randint(self.tamanio)
            horizontal = np.random.randint(2) == 1
            if self.colocar_barco(barco, fila, columna, horizontal):
                return True
        return False

    # --- disparos ---------------------------------------------------------
    def recibir_disparo(self, coordenada):
        """Procesa un disparo sobre el tablero y marca el resultado en el array.

        Args:
            coordenada (tuple[int, int]): (fila, columna) del disparo.

        Returns:
            str: clave de MENSAJES: 'error_repetido', 'disparo_agua',
            'disparo_tocado' o 'disparo_hundido'.
        """
        fila, columna = coordenada
        if self.casillas[fila, columna] in (SIMBOLO_TOCADO, SIMBOLO_AGUA):
            return 'error_repetido'

        barco = self.ocupadas.get(coordenada)
        if barco is None:
            self.casillas[fila, columna] = SIMBOLO_AGUA
            return 'disparo_agua'

        barco.recibir_impacto()
        self.casillas[fila, columna] = SIMBOLO_TOCADO
        return 'disparo_hundido' if barco.esta_hundido() else 'disparo_tocado'

    def todos_hundidos(self):
        """Devuelve True si todos los barcos del tablero están hundidos."""
        return all(barco.esta_hundido() for barco in self.barcos)

    # --- visualización ----------------------------------------------------
    def mostrar(self, mostrar_barcos=False):
        """Devuelve el tablero como texto, con letras en las columnas y números en las filas.

        Args:
            mostrar_barcos (bool): True para enseñar los barcos (tablero propio),
                False para ocultarlos (tablero rival).

        Returns:
            str: el tablero listo para imprimir.
        """
        letras = [chr(ord('A') + i) for i in range(self.tamanio)]
        lineas = [
            "      " + "   ".join(letras),
            "    " + "----" * self.tamanio + "-",
        ]
        for f in range(self.tamanio):
            fila = f"{f + 1:2d} |"
            for c in range(self.tamanio):
                simbolo = self.casillas[f, c]
                if not mostrar_barcos and simbolo == SIMBOLO_BARCO:
                    simbolo = SIMBOLO_VACIO
                fila += f"  {simbolo} "
            lineas.append(fila)
        return "\n".join(lineas)
