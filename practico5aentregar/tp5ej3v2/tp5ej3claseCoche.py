from tp5ej3claseVehiculo import Vehiculo
#from tp5ej3claseCoche import Coche
#from tp5ej3camioneta import Camioneta
#from tp5ej3Bicicleta import Bicicleta
#from tp5ej3motocicleta import motocicleta




class Coche(Vehiculo):
    def __init__(self, color,ruedas,velocidad,cilindrada,combustible,distaciaRecorrida,relacionConsumoDistancia):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.combustible = combustible
        self.distaciaRecorrida = distaciaRecorrida
        self.relacionConsumoDistancia=relacionConsumoDistancia

    def get_velocidad(self):
        return (self.velocidad)

    def get_cilindrada(self):
        return (self.cilindrada)

    def cargarCombustible(self,combustible,tanqueAnterior):
         self.combustible=combustible+tanqueAnterior   #----------------->como acumulo, contra que sumo
         return self.combustible #solo para poder verlo en pantalla

    def recorrerDistancia(self,distanciaRecorrida,relacionConsumoDistancia,distancia):
         trayecto=relacionConsumoDistancia*distancia
         if trayecto > (distanciaRecorrida*relacionConsumoDistancia):
             return self.combustible-((distanciaRecorrida+trayecto)*relacionConsumoDistancia)

             #"revisar" urgente

         # ej:200 km * relacionConsumoDistancia
         # ej:200km *  0,5 l/km=100 km
