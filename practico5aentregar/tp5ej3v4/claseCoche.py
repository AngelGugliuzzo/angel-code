from claseVehiculo import Vehiculo
#from claseCoche import Coche
#from claseCamioneta import Camioneta
#from claseBicicleta import Bicicleta
#from claseMotocicleta import Motocicleta
from claseMotor import Motor
from claseRendimiento import Rendimiento

class Coche(Vehiculo):
    def __init__(self,vehiculo,motor,rendimiento ):
        Vehiculo.__init__(self,motor,rendimiento)
        self.vehiculo=vehiculo
        self.motor=motor
        self.rendimiento=rendimiento


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

