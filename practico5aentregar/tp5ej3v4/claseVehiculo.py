#from claseVehiculo import Vehiculo
#from claseCoche import Coche
#from claseCamioneta import Camioneta
#from claseBicicleta import Bicicleta
#from claseMotocicleta import Motocicleta
#from claseMotor import Motor
#from claseRendimiento import Rendimiento


class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color