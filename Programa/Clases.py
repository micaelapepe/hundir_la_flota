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
