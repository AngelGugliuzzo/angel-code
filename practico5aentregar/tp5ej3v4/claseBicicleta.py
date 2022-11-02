from claseVehiculo import Vehiculo
#from claseCoche import Coche
#from claseCamioneta import Camioneta
#from claseBicicleta import Bicicleta
#from claseMotocicleta import Motocicleta
#from claseMotor import Motor
#from claseRendimiento import Rendimiento


class Bicicleta(Vehiculo):   #preguntar por la bicicleta a motor, en tal caso, la ubiccion esta bien parametros
    def __init__(self,color,ruedas,tipo):  # cil y vel 0
            Vehiculo.__init__(self, color,ruedas)
            self.tipo=tipo

    def get_tipo(self):
        return self.tipo
