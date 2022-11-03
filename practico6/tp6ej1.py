#1.	Cree una jerarquía de herencia de Roedores: Raton, Gerbo, Hamster.
#a.	En la clase base, proporcione los métodos que son comunes a todos los roedores
# (comer, olfatear, correr, trepar), y redefina aquellos en las clases derivadas para que tengan
# diferentes comportamientos dependiendo del tipo específico de roedor
# (con hacer print de “Estoy comiendo como un Hamster” o cualquier otra acción, es suficiente).
#b.	Cree una lista con objetos hijos de Roedor, rellenelo con distintos tipos de roedores y llame a
# los métodos de la clase base para observar lo que ocurre (comer, olfatear, correr, trepar). Sacar una conclusión.
#c.	Empezando con la jerarquía anterior de Roedor, herede un HamsterAzul de Hamster, sobreescriba los métodos de la
# clase base y muestre que el código que llama a los métodos de clase base no necesitan cambiar para
# adecuarse al nuevo tipo.
#d.	Modifique Roedor para convertirlo en una clase base abstracta.

from abc import ABC, abstractmethod

class Roedores(ABC):
    def __init__(self):
        self.roedor = "roedor"

    @abstractmethod
    def comer(self):
        print("comiendo con los roedores")

    @abstractmethod
    def olfatear(self):
        print("olfateando el morfi")

    @abstractmethod
    def correr(self):
        print("corriendo de los gatos")

    @abstractmethod
    def trepar(self):
        print("trepando aboles para cazar pajaritos")


#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
class Raton(Roedores):

    def __init__(self):
        super(Raton, self).__init__()

    def olfatear(self):
        super(Raton, self).olfatear()

    def correr(self):
        super(Raton, self).correr()

    def comer(self):
        super(Raton, self).comer()

    def trepar(self):
        super(Raton, self).trepar()

#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
class Gerbo(Roedores):

    def __init__(self):
        super(Gerbo, self).__init__()

    def olfatear(self):
        super(Gerbo, self).olfatear()

    def correr(self):
        super(Gerbo, self).correr()

    def comer(self):
        super(Gerbo, self).comer()

    def trepar(self):
        super(Gerbo, self).trepar()

#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
class Hamster(Roedores):
    def __init__(self):
        super(Hamster, self).__init__()

    def olfatear(self):
        super(Hamster, self).olfatear()

    def correr(self):
        super(Hamster, self).correr()

    def comer(self):
        super(Hamster, self).comer()

    def trepar(self):
        super(Hamster, self).trepar()

#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

raton=Raton()
print(raton.roedor)
raton.comer()
raton.olfatear()
raton.correr()
raton.trepar()
print("  ")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print(" ")
gerbo=Gerbo()
print(gerbo.roedor)
gerbo.comer()
gerbo.olfatear()
gerbo.trepar()
gerbo.correr()
print("  ")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print(" ")
hamster=Hamster()
print(hamster.roedor)
hamster.comer()
hamster.olfatear()
hamster.trepar()
hamster.correr()