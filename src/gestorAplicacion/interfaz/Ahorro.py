# Ana Guarín
# Isabela Hernandez
# Cristian Menaa
# Julián Álvarez

from gestorAplicacion.interfaz.Cuenta import Cuenta
from datetime import date

class Colchon(Cuenta):

    def __init__(self, usuario, nombre, fechaRetiro):
        super().__init__(usuario, nombre)
        self._fechaRetiro = fechaRetiro

    def retirar(self, monto):
        if self._fechaRetiro.isBefore(date.today()):
            return super().retirar(monto)
        return False

    def getFechaRetiro(self):
        return self._fechaRetiro

    def setFechaRetiro(self, fechaRetiro):
        self._fechaRetiro = fechaRetiro
