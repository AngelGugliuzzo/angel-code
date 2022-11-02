#1.	Se solicita implementar una o varias clases que nos permita controlar un tablero electronico de basquet, por lo tanto:
#a.	Crear una clase TableroDeBasquet el cual tendrá como atributos: local (string), visitante (string),
# puntos_local (entero), y puntos_visitante (entero).
#b.	Crear un método que adicione puntos de a 3, tanto al local como al visitante
#c.	Crear un método que adicione puntos de a 2, tanto al local como al visitante.
#d.	Crear un método que adicione puntos de a 1, tanto al local como al visitante.
#e.	Analizar si es conveniente guardar el puntaje y el nombre del equipo en la instancia
# del TableroDeBasquet o si es mejor generar otra clase llamada Equipo y guardar la información en esas instancias
# de la clase Equipo

import frase2
class TableroDeBasquet:
    def __init__(self,local,visitante,puntos_local, puntos_visitante):

        self.local = local
        self.visitante = visitante
        self.puntos_local = puntos_local
        self.puntos_visitante = puntos_visitante

    def adicionarDeAtresVisitante(self):
        self.puntos_visitante += 3

    def adicionarDeAtresLocal(self):
        self.puntos_local += 3

    def adicionarDeAdosVisitante(self):
        self.puntos_visitante += 2

    def adicionarDeAdosLocal(self):
        self.puntos_local += 2

    def adicionarDeAunoVisitante(self):
        self.puntos_visitante +=  1

    def adicionarDeAunoLocal(self):
        self.puntos_local = self.puntos_local + 1

    def __str__(self):
        return "visitante:{} local:  {}".format(self.visitante, self.local)

    def set_puntosLocales(self):
        self.puntos_local=0 #---------------->inicializa con 0

    def set_puntoVisitante(self,puntos_visitante):
        return self.puntos_visitante

    def get_puntosLocales(self):
        return self.puntos_local

    def get_puntosVisitante(self):
        return self.puntos_visitante

tablero=TableroDeBasquet("asta sa bc ","los pancracios bc ",0,0)

#tablero.puntos_visitante=1
#tablero.puntos_local=1

tablero.adicionarDeAtresVisitante()

tablero.adicionarDeAunoLocal()

tablero.adicionarDeAunoVisitante()

tablero.adicionarDeAdosLocal()

tablero.adicionarDeAunoVisitante()

tablero.adicionarDeAtresLocal()

tablero.adicionarDeAtresVisitante()



print(" ")
print(" ")
print("visitantes : "+tablero.visitante,"  locales : "+tablero.local)
print("----------                        -------")
print("                 ",tablero.get_puntosVisitante(),"                           ",tablero.get_puntosLocales())

#import frase2



        