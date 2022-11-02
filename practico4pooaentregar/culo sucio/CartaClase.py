import random
#import CartaClase
import claseMazo
import clasejugador

class Carta:
    def __init__(self, valor, palo, orden):
        self.valor = valor
        self.palo = palo
        self.orden = orden

    def es_1_de_oro(self):
        return True