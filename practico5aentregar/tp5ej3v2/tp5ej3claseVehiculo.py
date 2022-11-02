#from tp5ej3claseVehiculo import Vehiculo
#from tp5ej3claseCoche import Coche
#from tp5ej3camioneta import Camioneta
#from tp5ej3Bicicleta import Bicicleta
#from tp5ej3motocicleta import motocicleta



class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color

