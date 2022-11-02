from claseVehiculo import Vehiculo
from claseCoche import Coche
#from claseCamioneta import Camioneta
#from claseBicicleta import Bicicleta
#from claseMotocicleta import Motocicleta
from claseMotor import Motor
from claseRendimiento import Rendimiento


class Camioneta(Coche):
    def __init__(self, vehiculo, motor, rendimiento,carga):
        Coche.__init__(self,vehiculo, motor, rendimiento)
        self.vehiculo = vehiculo
        self.motor = motor
        self.rendimiento = rendimiento

        self.carga = carga

    def get_carga(self):
        return self.carga