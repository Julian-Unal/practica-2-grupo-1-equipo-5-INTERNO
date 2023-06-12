
# Ana Guarín
# Isabela Hernandez
# Cristian Menaa
# Julián Álvarez

from enum import Enum

class Categoria (Enum):
	Viajes=(0, 0)
	Salud=(0,0)
	Alimentacion=(0,0)
	Transporte=(0,0)
	Educacion=(0,0)
	Hogar=(0,0)
	Entretenimiento=(0,0)
	Imprevistos=(0,0)
	Nulo=(0,0)

	def __init__(self, saldo, presupuesto):
		self._saldo = saldo
		self._presupuesto = presupuesto

	def getSaldo(self):
		return self._saldo
	
	def setSaldo(self, saldo):
		self._saldo = saldo
		
	def getPresupuesto(self):
		return self._presupuesto
	
	def setSaldo(self, presupuesto):
		self._presupuesto = presupuesto

listaCat = list(Categoria)


# Imprimir el contenido del array
for cat in listaCat:
	print(cat)