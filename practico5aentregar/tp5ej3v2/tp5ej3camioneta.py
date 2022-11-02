from tp5ej3claseVehiculo import Vehiculo
from tp5ej3claseCoche import Coche
#from tp5ej3camioneta import Camioneta
#from tp5ej3Bicicleta import Bicicleta
#from tp5ej3motocicleta import motocicleta



class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga,combustible,distaciaRecorrida,relacionConsumoDistancia):  # --------------->no puedo pasarlos color y ruedas
        Coche.__init__(self,color,ruedas,velocidad,cilindrada,combustible,distaciaRecorrida,relacionConsumoDistancia) #probe con coche, da lo mismo.
        self.carga = carga

    def get_carga(self):
        return self.carga



