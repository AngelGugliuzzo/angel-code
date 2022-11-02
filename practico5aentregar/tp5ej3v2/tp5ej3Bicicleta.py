from tp5ej3claseVehiculo import Vehiculo
#from tp5ej3claseCoche import Coche
#from tp5ej3camioneta import Camioneta
#from tp5ej3Bicicleta import Bicicleta
#from tp5ej3motocicleta import motocicleta


class Bicicleta(Vehiculo):   #preguntar por la bicicleta a motor, en tal caso, la ubiccion esta bien parametros
    def __init__(self,color,ruedas,tipo):  # cil y vel 0
            Vehiculo.__init__(self, color,ruedas)
            self.tipo=tipo

    def get_tipo(self):
        return self.tipo


