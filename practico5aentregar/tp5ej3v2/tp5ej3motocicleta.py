from tp5ej3claseVehiculo import Vehiculo
from tp5ej3claseCoche import Coche
#from tp5ej3camioneta import Camioneta
#from tp5ej3claseVehiculo import Vehiculo
#from tp5ej3claseCoche import Coche


class Motocicleta(Coche):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada,combustible,distaciaRecorrida,relacionConsumoDistancia):
            Coche.__init__(self, color,ruedas,tipo,velocidad,cilindrada,distaciaRecorrida,relacionConsumoDistancia)
            self.tipo=tipo


    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.cilindrada




