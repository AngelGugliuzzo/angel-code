import Vehiculo
import Coche

class Bicicleta(Vehiculo):
         def __init__(self,tipo):  # --------------->no puedo pasarlos color y ruedas
            Vehiculo.__init__(self, tipo)
            self.tipo = tipo

        def get_tipo(self):
            return self.tipo



