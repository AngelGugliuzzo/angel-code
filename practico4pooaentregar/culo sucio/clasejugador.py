import random
import CartaClase
import claseMazo
import ClaseJuego

class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        #self.apellido = apellido
        #self.telefono = telefono


    def sacar_carta(self):
        if len(self.cartas) > 0:
               print("No está vacía")
               return self.cartas.pop()
        else:
            print("Está vacía")
