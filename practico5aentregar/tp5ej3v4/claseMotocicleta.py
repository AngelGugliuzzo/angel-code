from claseVehiculo import Vehiculo
from claseCoche import Coche
#from claseCamioneta import Camioneta
#from claseBicicleta import Bicicleta
#from claseMotocicleta import Motocicleta
from claseMotor import Motor
from claseRendimiento import Rendimiento


class Motocicleta(Coche):
    def __init__(self, vehiculo, motor, rendimiento, tipo):
        Coche.__init__(self, vehiculo, motor, rendimiento)
        self.vehiculo = vehiculo
        self.motor = motor
        self.rendimiento = rendimiento

        self.tipo=tipo

    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.cilindrada

