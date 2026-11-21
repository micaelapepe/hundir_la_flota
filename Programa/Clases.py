import numpy as np

from variables import *

class Barcos:
	def __init__(self, longitud):
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
		return self.impactos >= self.longitud
    
#-- CLASE TABLERO

class Tablero:
    def __init__(self, tamanio=TAMANIO_TABLERO):
        self.tamanio = tamanio
        self.casillas = np.full((tamanio, tamanio), SIMBOLO_VACIO)
        self.barcos = []
        self.ocupadas = {}        # (fila, columna) -> Barco

    # --- colocación -------------------------------------------------------
    def _en_limites(self, fila, columna):
        return 0 <= fila < self.tamanio and 0 <= columna < self.tamanio

    def _hay_barco_cerca(self, fila, columna):
        
        for df in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (fila + df, columna + dc) in self.ocupadas:
                    return True
        return False

    def puede_colocar(self, posiciones):
        
        return all(
            self._en_limites(f, c) and not self._hay_barco_cerca(f, c)
            for f, c in posiciones
        )

    def colocar_barco(self, barco, fila, columna, horizontal):
       
        posiciones = [
            (fila, columna + i) if horizontal else (fila + i, columna)
            for i in range(barco.longitud)
        ]
        if not self.puede_colocar(posiciones):
            return False
        barco.posiciones = posiciones
        for posicion in posiciones:
            self.ocupadas[posicion] = barco
        self.barcos.append(barco)
        return True

    def colocar_barco_aleatorio(self, barco, intentos=1000):
        for _ in range(intentos):
            fila = np.random.randint(self.tamanio)
            columna = np.random.randint(self.tamanio)
            horizontal = np.random.randint(2) == 1
            if self.colocar_barco(barco, fila, columna, horizontal):
                return True
        return False

    # --- disparos ---------------------------------------------------------
    def recibir_disparo(self, coordenada):
        
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
        return all(barco.esta_hundido() for barco in self.barcos)

    # --- visualización ----------------------------------------------------
    def mostrar(self, mostrar_barcos=False):
        
        letras = [chr(ord('A') + i) for i in range(self.tamanio)]
        lineas = [
            "      " + "   ".join(letras),
            "    " + "----" * self.tamanio + "-",
        ]
        for f in range(self.tamanio):
            fila = f"{f + 1:2d} |"
            for c in range(self.tamanio):
                simbolo = self.casillas[f, c]
                if mostrar_barcos and simbolo == SIMBOLO_VACIO and (f, c) in self.ocupadas:
                    simbolo = SIMBOLO_BARCO
                fila += f"  {simbolo} "
            lineas.append(fila)
        return "\n".join(lineas)
